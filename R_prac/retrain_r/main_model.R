## create a model - load in a different file 
set.seed(1010)
library(tidyverse)
library(caret)
library(CARS)
library(remake)  # for pipeline 
require(drake)
library(jsonlite)
library(httr)
library("dplyr")
library("tidyr")

## register model in model manager 

# use model manager api's and tokens for this - ie https://gitlab.sas.com/api-docs/api-documentation-crowd-sourcing/-/blob/master/R/automl-end-to-end/mlpa-end-to-end.ipynb


## use plumber to host api to retrain the model, deployed & register the model  - retrain as api. Also a separate location for where the model can be accessed

## host on docker/k8s cluster  https://www.rplumber.io/articles/hosting.html#docker-basic-

##########################
# score our model in mas #
##########################

# to connect to our instance of viya 
source("auth_func.r")

host <- "viya-instance"
client_name <- "client_name"
client_secret <- "r_secret"

linez <- readLines('.authinfo')
username <- linez[1]
password <- linez[2]
host <- linez[3]

tokenDetailed <- authenticate(host = host,
                              username = username,
                              password = password,
                              client_name = client_name,
                              client_secret = client_secret)

token <- tokenDetailed$access_token

# retreiving mas models 
masModules <- function(finalToken,
                       host,
                       start_index = 0,
                       return_limit = 20) {
  url <- parse_url(host)
  url$path <- "/microanalyticScore/modules/"
  
  # additional api filters 
  url$query <- list(
    "start" = start_index,
    "limit" = return_limit
  )
  
  response <- GET(
    url = build_url(url),
    add_headers(
      "Accept" = "application/json",
      "Authorization" = paste("Bearer", token)
    )
  )
  
  stop_for_status(response)
  
  # there is more to the request but we don't need it 
  modules <- fromJSON(content(response, as = "text"))$items
  return(modules)
}

modules <- masModules(token, host)

# remove not needed info 
modules <- subset(modules, select = -c(links, properties, warnings))

# modules info 
modules

# retreiving model input/outpus 
moduleFeatures <- function(moduleId, token, host) {
  url <- parse_url(host)
  url$path <- paste0('microanalytics/modules/', moduleId, '/steps')
  
  response <- GET(
    url = build_url(url),
    add_headers(
      # content-type = "application/x-www-form-urlencoded",
      "Accept" = "application/json",
      "Authorization" = paste("Bearer", token)
      
    )
  )
  
  stop_for_status(response)
  features <- fromJSON(content(response, as = "text"))$items
  return(features)
}

modulename <- "dt_hmeq"
features <- moduleFeatures(modulename, token, host)

features$inputs 
features$outputs 



# scoring data
df <- read.csv("./data/hmeq.csv")
df[df == ''] <- NA
df <- na.omit(df)
colnames(df) <- tolower(colnames(df))

df_treated <- df[, features$inputs[[1]]$name]

# execution 
scoreModule <- function(moduleId, token, host,
                        data_json) {
  url <- parse_url(host)
  url$path <- paste0('microanalyticScore/modules/', moduleId, '/steps/score')
  
  response <- POST(build_url(url),
                   add_headers(
                     "Content-Type" = "application/json",
                     "Authorization" = paste("Bearer", token)
                   ),
                   body = data_json,
                   encode = 'json'
  )
  stop_for_status(response)
  scored <- fromJSON(content(response, as = "text"))
  return(scored)
  
}

##Preparing the data to the expected format:

list_json <- head(df_treated) %>% ### doing only first 6
  mutate(id = row_number()) %>%
  pivot_longer(cols = -id) %>%
  split(x = .[-1], f = .$id) %>%
  unname %>%
  lapply( function(x) toJSON(list(inputs = x)))


### scoring all rows
batch_score <- lapply(list_json, function(x) scoreModule("dt_hmeq", 
                                                         token,
                                                         host,
                                                         data = x))
