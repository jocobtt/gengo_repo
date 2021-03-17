# Concept of this blog:

- introduce Azureml
- show how to set up environment/other tricks and tips 
- show different integration points with SAS - walk through a quick usecase


# What is AzureML?
With SAS and Microsoft's partnership that was announced this year in June(?) there has been a consistent effort put in from all groups to better learn Azure's vast suite of offerings. One offering in Azure's services that is particularly interesting that has some pivital integration points with SAS is Azure Machine Learning, or AzureML for short. AzureMl is "a cloud-based environment you can use to train, deploy, automate, manage, and track ML models." (https://docs.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-ml) AzureML has R and Python SDK's or you can use Azure machine learning studio for no-code/low-code options as well. With AzureML you can start training your models on your local machine and scale out to the cloud as needed to effeciently train and deploy models for your various workflows. In this blog I will show how to set up an AzureML environment for running your machine learning models, how to seamlessly transition your model training to a customizeable environment in Azure, and how to integrate your trained models with SAS Model Manager to better fit into the ModelOps lifecycle that allows you to better operationalize your analytics. 

# Set up environment 
Setting up your environment in AzureML can be accomplished via Azure's CLI or either the R or Python SDK's locally, or can be done via the Azure Portal UI. For this blog I will show how to do it through the Python SDK. For this example we will be building a simple light gradient boost model in Python and training it on the hmeq loan dataset and deploy it to both model manager and azure. We will also create an R model and likewise register that to model manager and use the azureml sdk for R to train a caret gradient boosting model. 

For using any service in Azure we first need a resource group to associate the service with. Resource groups are how you logically separate resources in Azure** and by specifying what the resource owner is in the tags it helps with keeping track of who owns what resources and allows you to be a better citizen in your organizations cloud environment.  

Through the azureml package we can create a resource group and a workspace to associate our azureml workloads with. 

```python
from azureml.core import Workspace

ws = Workspace.create(name='example-workspace',
                       subscription_id='my-sub-id', # can find this either through the Azure UI or through running "az account show --query id"
                       resource_group = "azureml-rg", # can either use resource group we've already made or create a new one and define the name here
                       location = 'eastus'
                       )

# write our workspace configuration information to a directory specified below 
ws.write_config(path='.azureml')
```

Likewise in R to create our environment we would do the following:
```R
library(azuremlsdk)

# make/connect to our environment 
ws <- azuremlsdk::create_workspace(
  name = "R-workspace",
  subscription_id = "my-sub-id", 
  create_resource_group = TRUE,
  location = 'eastus'
)
ws
azuremlsdk::write_workspace_config(workspace = "R-workspace", path = ".r-azureml")
```


Now that we have created our workspace we can now use the configuration to then create our compute environment to train our code in. 

For sepcifying the python packages needed for the environment we define that through creating an `.azureml` directory somewhere in our local file system that we will map to in our python commands. Inside this folder we have various yaml files for each environment that we may want to use. For instance if we wanted to create an environment for our previously introduced model we would create a yaml file like below. 

```yaml
name: sci-kit-env
channels:
    - defaults
    - scikit
dependencies:
    - python=3.8.6
    - scikit-learn
    - numpy 
    - pip:
      - azureml-defaults 
      - sasctl
      - swat
      - lightgbm
```
As we can see from above the yaml file is defining the name of the environment, the channels that are needed - define channels, and the dependencies including the Python version, what packages to install via pip and what other pre set values are needed. This file will be used to configure out environment that will be spun up in our workspace that we provisioned earlier. 

In order to then use the above defined environment we are going to call out the environment that we are going to use by using the below code:
```python
from azureml.core import Environment

myenv = Environment(".azureml/sas-env.yaml")

# if we want to add more features... 
# create our env inside a docker container 
myenv.docker.enabled = True 
# use a prebuilt docker image 
myenv.docker.base_image = "Our-image"
myenv.docker.base_dockerfile = "registry_location"
# use a custom dockerfile 
dockerfile = r"""
FROM blah 
RUN blah 
"""
myenv.docker.base_image = None 
myenv.docker.base_dockerfile = dockerfile 
# use a conda environment 
myenv = Environment.from_existing_conda_environment(name="myenv",
                                                    conda_environment_name="mycondaenv")

```

Creating a custom environment for R is a bit different in that we can't create a yaml file for our desired packages for our environment like we can in python. Azureml provides an R environment that comes pre-built with plenty of libraries. We can obviously create a docker image to run our needed r packages on top of what Azure provides or we can install our needed packages directly to our azureml provisioned vm. 

```R
FROM mcr.microsoft.com/azureml/base:openmpi3.1.2-ubuntu18.04
RUN conda install -c r -y pip=20.1.1 openssl=1.1.1c r-base rpy2 && \
  conda install -c conda-forge -y mscorefonts && \
  conda clean -ay && \
  pip install --no-cache-dir azureml-defaults
  
ENV TAR="/bin/tar"
RUN R -e "install.packages(c('remotes', 'reticulate', 'optparse'), repos = 'https://cloud.r-project.org/')"
RUN R -e "remotes::install_github('https://github.com/Azure/azureml-sdk-for-r')"

env <- r_environment("r-env", custom_docker_image = "<username/<repo>:<tag>")
```

# Create script to train our model 
One of the ways that we can use azureml is to have it run our model training code so that we have the ability to scale up, customize our environment and have a dedicated location where our model would train at. Although this isn't always necessary or what is best, it still allows you to be able to free up resources for other computing jobs. You can also choose to train the script locally and store the model weights in a way that it can then be used by Azureml and Model Manager later on, ie pickling or zipping your model. 

For our example we are going to be creating a script to train a gradient boosting model on the hmeq loan dataset to help us predict who is likely to default on a loan or not. For this we are going to first define our model below and then from there use azureml to run our training script in our provisioned Azure environment. 

```python
import lightgbm as lgb 
import pandas as pd 
import os 
import pickle 
from sklearn.model_selection import train_test_split 

df = pd.read_csv('http://support.sas.com/documentation/onlinedoc/viya/exampledatasets/hmeq.csv', sep = ',')

df = df.drop(columns = ['JOB', 'REASON'], axis = 1)
df = df.fillna(df.mean())
# split the data into train and test 
X = df.iloc[:, 1:]
y = df.iloc[:, :1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state = 303)

# set number of number of features and number of training sets 
num_train, num_feature = X_train.shape

# set feature names 
feature_name = ['feature_' + str(col) for col in range(num_feature)]

lgb_train = lgb.Dataset(X_train, y_train, free_raw_data=False)
lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train, free_raw_data=False)

# set parameters 
params = {
    'boosting_type': 'gbdt',
    'seed': 101,
    'objective': 'binary',
    'metric': 'auc',
    'num_leaves': 25,
    'learning_rate': 0.05,
    'feature_fraction': 0.6,
    'bagging_fraction': 0.4,
    'bagging_freq': 3,
    'verbose': 1
}

gbm_mod = lgb.train(params,
                      lgb_train,
                      num_boost_round = 10,
                      valid_sets = lgb_train, # eval training data
                      feature_name = feature_name,
                      categorical_feature = [21])

# dump model with pickle
with open('model.pkl', 'wb') as fout:
  pickle.dump(gbm_mod, fout)

# load with pickle to predict 
with open('model.pkl', 'rb') as fin:
  pkl_bst = pickle.load(fin)

# can predict with any iteration when loaded in pickle way 
y_pred = pkl_bst.predict(X_test, num_iteration=7)

```

Now to explain a little bit about what is going on, we are using the lightgbm python package to create a gradient boosting model. We are doing some simple feature name setting, partitioning the data for testing and training, fitting our model and then saving said model to a pickle file. With this training file we can then use Azureml to run this script for us and store the pickle object to model manager and or Azureml as needed or desired. 

```python 
# create compute cluster - add part to make it be a gpu enabled cluster 
#os.chdir("/models/")
#ws = Workspace.from_config(".azureml")   # this is using a workspace that we've already created and is loaded in for us

# name for our cpu cluster 
cluster_name = 'gpu-cluster'

# verify cluster doesn't already exist 
# if want large cpu instead of gpu use 'STANDARD_D2_V2' as our image 

try:
    cpu_cluster = ComputeTarget(workspace=ws, name=cluster_name)
    print('Found existing cluster, use it.')
except ComputeTargetException:
    compute_config = AmlCompute.provisioning_configuration(vm_size='STANDARD_NC6',
                                                           min_nodes=1,
                                                           max_nodes=4, 
                                                           idle_seconds_before_scaledown=2400)
    cluster = ComputeTarget.create(ws, cluster_name, compute_config)

cluster.wait_for_completion(show_output=True, min_node_count=1, timeout_in_minutes=20)

# configure and run 
src = ScriptRunConfig(source_directory='.',
                      script = 'model.py',
                      compute_target=cluster, 
                      environment = myenv)
run = experiment.submit(config=src)
run
```

# Integration points with Viya

There are a few ways that you can integrate SAS with Azureml. You can use either the sasctl package to help you with registering, deploying and monitoring models using SAS Model Manager. Or you can use Swat to connect with Viya and interact with Cas to create a sas model through python or R. You can also use Swat to do data prep and feature engineering for your model. 

An example of how you could use sasctl with Azureml is to use azureml to handle execution of the training of our model but then sending our model artifacts to Model Manager and then deploying said model to a choosen runtime from Model Manager - in our case our mas runtime. Below we connect to our Viya instance using the sasctl python package. From there we will create our model and input the various information that we need for model manager - who created the model, what model we created, what algorithm was used and other information we want to input. We then read in each of our files - our training file created above, our pickle file created from our training script and various model metadata json files. We then add each of those items to our model manager repository that we just created using the sasctl package. With our model now registered with our needed files we can now deploy our model to the maslocal destination below. 

```python
import swat 
from sasctl import Session, publish_model, register_model, update_model_performance
from sasctl.services import model_repository as mr 
from sasctl.services import model_management as mm 
from sasctl.services import model_publish 
import getpass 

# set environment variables to use sasctl - for ssl
os.environ['CAS_CLIENT_SSL_CA_LIST'] = '/Users/jabras/Work/cicd_ops/azure_ml/trustedcerts.pem'
os.environ['TKESSL_OPENSSL_LIB'] = '/lib/x86_64-linux-gnu/libssl.so.1.0.0'
os.environ['LD_LIBRARY_PATH'] = 'lib/x86_64-linux-gnu/libssl.so.1.0.0'

 # set argument variables for sasctl 
ENV = 'gtpv4-cas.unx.sas.com'
USER = 'jabras'
P = getpass.getpass()

# start our session 
Session(ENV, USER, P, verify_ssl=False, protocol='http')

 # create model 
model_repository.create_model(model = 'GB',
                             project = 'Azureml',
                             modeler = 'Jacob Braswell',
                             algorithm = 'Gradient Boosting',
                             tool = 'Python',
                             score_code_type='Python',
                             training_code_type='Python'
                             function='Classification',
                             is_champion=True)

 filenames = {'file':['inputVar.json','outputVar.json','train_lgb.py','model.pkl', 'fileMetadata.json', 'ModelProperties.json'],
            'role':['input','output', 'score', 'score resource', 'file metadata', 'model properties']}

for i in range(len(filenames['file'])):
    with open(path / filenames['file'][i], "rb") as _file:
        model_repository.add_model_content(
                      model = 'GB', 
                      file = _file, 
                      name = filenames['file'][i], 
                      role= filenames['role'][i])        
        print('uploaded ' + filenames['file'][i] + ' as ' + filenames['role'][i])
        _file.close()
# publish our model 
 publish_model('GB', 'maslocal')
```


If we are instead wanting to deploy our model to an Azure Kubernetes Service cluster instead of docker images or on a traditional vm endpoint, for the purposes of scalability and orchestration, we can use an Azure Kubernetes Service cluster for our deployment destination. In order to do so you can refer to this [README](https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/machine-learning/how-to-deploy-azure-kubernetes-service.md)

A second example is using swat to run an end to end data science project. Since Azureml can also handle R code we will use the R based Swat package for this example. For R Azure has also made an SDK for the azureml so we will utilize that for this example. What we will first do is create a CAS model using the Swat R package, for this example we will create a simple decision tree that we will then train in Azure. 

First we are going to create a simple R model like we did above in Python. This model object will be saved as an R file. We are using the caret R package which allows us to create our model and as well as other functions necessary to get an accurate model for our purposes. In the below code we are also saving our model values as an RDS file and then registering it to Azureml as well. 

https://azure.github.io/azureml-sdk-for-r/reference/register_model_from_run.html

```R
library(tidyverse)
library(caret)
library(DataExplorer)

set.seed(101)
df <- read.csv('http://support.sas.com/documentation/onlinedoc/viya/exampledatasets/hmeq.csv')

# drop reason and job 
drop <- c("REASON", "JOB")
df = df[!(names(df) %in% drop)]

# deal with missing values - fill with column means 
for(i in 1:ncol(df)){
  df[is.na(df[,i]), i] <- mean(df[,i], na.rm = TRUE)
}

# set bad as factor 
df$BAD <- df$BAD %>% as.factor

# partition the data 
part <- caret::createDataPartition(df$BAD, p = .75, list = FALSE)
train <- df[part,]
test <- df[-part,]

# set way we want to resample - figure out how to make this model a classification type 
fit_cont <- caret::trainControl(
  method = "cv",
  number = 5
)

gbm_fit <- caret::train(
  form = BAD ~., 
  data = train,
  trControl = fit_cont,
  method = "xgbTree"
)

summary(gbm_fit)

# save our model 
saveRDS(gbm_fit, "model.rds")
gbm_mod <- readRDS("model.rds")

# register our model in Azure environment 
model <- register_model_from_run(run,
                                 model_path='outputs/my_model.rds',
                                 model_name='my_model')
# register our model in Model Manger 

```

Now that we have created our model in a separate file we are going to now create our Azure environment and push our above created R model to our Azure environment. 

```R
library(azuremlsdk)
library(tidyverse)
library(caret)
library(swat)

# https://github.com/revodavid/mlops-r/blob/master/azuremlsdk-vignettes/experiments-with-R.pdf
# https://rstudio.com/resources/rstudioconf-2020/mlops-for-r-with-azure-machine-learning/
# https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-1st-r-experiment
# https://github.com/Azure/azureml-sdk-for-r/tree/master/samples

# make/connect to our environment 
ws <- load_workspace_from_config()
ws

# mess with the environment - https://azure.github.io/azureml-sdk-for-r/reference/r_environment.html

experiment_name <- "hmeq_logreg"
exp <- experiment(ws, experiment_name)

# create compute target 
cluster_name <- 'rclust'
compute_target <- get_compute(ws, cluster_name = cluster_name)
if (is.null(compute_target)) {
  vm_size <- "STANDARD_D2_V2"
  compute_target <- create_aml_compute(
    workspace = ws,
    cluster_name = cluster_name,
    vm_size = vm_size,
    vm_priority = '"lowpriority',
    min_nodes = 1,
    max_nodes = 3
) 
}
wait_for_provisioning_completion(compute_target)

# train and deploy our swat model 
est <- estimator(
  source_directory = ".",
  entry_script = "azureml_swat.R",
  script_params = list("--data_folder" = ds$path(target_path)),
  compute_target = compute_target
)
run.swat <- submit_experiment(exp, est)

metrics <- get_run_metrics(run.swat)
metrics

# train and deploy our caret model 

# deploy model as service 
model <- register_model(ws, model_path = "model.rds", model_name = "model.rds")  # use a script instead of a saved model 

# set our environment
swat_env <- r_environment(
  name = "swat_env", 
  version = "1.0",
  cran_packages = list("tidyverse",
                       "caret"),
  github_packages = "sassoftware/R-swat"
)

inference_config <- inference_config(
  entry_script = "hmeq_care.R",
  source_directory = ".",
  envrionment = caret_env
)

aci_config <- aci_webservice_deployment_config(
  cpu_cores = 1,
  memory_gb = 0.5
)

aci_service <- deploy_model(
  ws,
  'hmeq-caret',
  list(model),
  inference_config,
  aci_config
)

wait_for_deployment(service, show_output = TRUE)

crat.endpoint <- get_webservice(
  ws,
  'hmeq-caret'
)$scoring_uri


# test inference of our model 
test <- data.frame(LOAN = 1600,
                   MORTDUE = 20834,
                   VALUE = 105384,
                   YOJ = 13,
                   DEROG = 1,
                   DELINQ = 3,
                   CLAGE = 150,
                   NINQ = 10,
                   CLNO = 12,
                   DEBTINC = 33.8)

# test the web service 
predicted_val <- invoke_webservice(service, toJSON(test))
predicted_val

# clean up 
delete_webservice(service)

delete_model(model)

delete_compute(compute)

```

Now that we have trained our model and registered it in Azureml we can now do the same in SAS using our R-Swat model that we have trained above. https://gitlab.sas.com/api-docs/api-documentation-crowd-sourcing/-/tree/master/R

```R
library(swat)
library(azuremlsdk)
library(httr)
library(jsonlite)
set.seed(101)

host <- "blah.sas.com"
auth_user <- "username"
auth_pass <- "pass"
dataset_name <- "hmeq"
target <- "BAD"
public_uri <- "/dataTables/dataSources/cas~fs~cas-shared-default~fs~Public/tables/"

project_name <- past(dataset_name, "-", UUIDgenerate(), sep = "")
auth_cred <- paste("password&username=", auth_user, '&password=', auth_pass, sep = "")

token_uri <- "SASLogon/oauth/token"
payload <- paste("grant_type=", 'password&username=', auth_user, '&password=', auth_pass, sep = "")

url <- paste(url_prefix, token_uri, '?', payload, sep = "")
body <- payload

response <- POST(url, add_headers(.headers = c("Content-Type"="application/x-www-form-urlencoded", "accept"="application/json", "authorization"="Basic c2FzLmVjOg==")), verbose)
json_resp_parsed <- content(response, as="parsed")

oauth_token <- paste('Bearer', json_resp_parsed$access_token)
token_uri <- "/mlPipelineAutomatation/projects"
url <- paste(url_prefix, token_uri, sep = "")

data_table_uri <- paste(public_uri, dataset_name, sep = "")

body <-paste('{"dataTableUri": "',data_table_uri,
'","type": "predictive",
"name": "', project_name,
'","description": "Project generated for test",
"settings": {"autoRun": true, "maxModelingTime": 15},
"analyticsProjectAttributes": {"targetVariable": "',target,'"}}', sep="")

response <- POST(url,
add_headers(.headers = c("Authorization"= oauth_token,"Content-Type"="application/json","Accept"= "application/vnd.sas.analytics.ml.pipeline.automation.project+json")),
body=body)
mlpa_project<-fromJSON(content(response,as="text"))
```

# Conclusion
As shown through this blog there are tons of ways in which Azure with Viya help to operationalize analytics in whatever method that makes the most sense for the user. Whether its registering and deploying a model using SAS, exposing a model via Azure, using Azure to train your model, or any other workflow that makes the most sense to the user. With this flexiblity it allows the user to not have to worry about managing multiple models or deal with the headache of how many machines they need to provision or even getting the right dependencies for their runtime environment set up, that is all able to be controlled from one central location and source. 
