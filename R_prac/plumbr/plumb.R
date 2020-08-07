library("plumber")

# https://www.rplumber.io/articles/hosting.html
# https://rviews.rstudio.com/2018/07/23/rest-apis-and-plumber/

# load in the model
test_mod <- readRDS('air.rds')

#* @apiTitle air model API
#* @apiDescription Endpoints for working with airquality dataset model

#* log some info about incoming request
#* @filter logger 


