# api setup 
library(plumber)

alive <- TRUE

# read model data 

model <- readRDS(file = 'cars.rds')

# https://medium.com/tmobile-tech/r-can-api-c184951a24a3
# https://juanitorduz.github.io/intro_plumber/
# https://anderfernandez.com/en/blog/how-to-put-an-r-model-in-production/
# https://github.com/sol-eng/plumber-model
# https://anderfernandez.com/en/blog/how-to-put-an-r-model-in-production/
# https://mdneuzerling.com/post/hosting-a-plumber-api-with-kubernetes/
# https://cran.r-project.org/web/packages/AzureContainers/vignettes/vig01_plumber_deploy.html
# https://mdneuzerling.com/post/hosting-a-plumber-api-with-kubernetes/ **
# https://www.rplumber.io/articles/hosting.html#docker-basic-
# https://github.com/blairj09/plumber-playground/tree/master/experiments
# https://github.com/blairj09/plumber-demo

## filter-logger 
#* log some info about the incoming request
#* @filter logger 
function(req){
  cat(as.character(Sys.time()), "-",
      req$REQUEST_METHOD, req$PATH_INFO, "-",
      req$HTTP_USER_AGENT, "@", req$REMOTE_ADDR, "\n")
  forward()
}

#* Clean up cookie
#* @filter clean-cookie
function(req, res) {
  if (!is.null(req$cookies$data)) {
    print(paste("Data cookie:", req$cookies$data))
    print(paste("Clean cookie:", stringr::str_extract(req$cookies$data, "\\[.*\\]")))
    if (req$cookies$data != 0) {
      # Clean up cookie (issue with leading and trailing " when deployed to RSC)
      req$cookies$data <- stringr::str_extract(req$cookies$data, "\\[.*\\]|^0$")
    }
  }
  
  print(paste("Cleaned Data cookie:", req$cookies$data))
  
  forward()
}


## post-data
#* submit data & get a prediction in return 
#* @post /predict
function(req, res) {
  data <- tryCath(jsonlite::parse_json(req$postBody, simplifyVector = TRUE),
                  error = function(e) NULL)
  if (is.null(data)) {
    res$status <- 400
    return(list(error = "No data submitted"))
  }
  
  predict(cars_model, data)
}

## post for different model 
#* @post /pred_cars 
function(req, res) {

}


## retrain model somehow - preferribly through drake - https://gitlab.sas.com/ssayjc/python-retrain-as-api/-/blob/master/app/api.py
#* @post /retrain
function(req, res) {
  
}




