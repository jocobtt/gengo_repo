# pipeline using drake 
# https://github.com/ropensci/drake
# https://github.com/wlandau/drake-examples

library(drake)

source("drake/packages.R")
source("drake/functions.R")
source("drake/plan.R")

ls()

drake::make(my_plan, jobs = 2)
# or can run drake_config(my_plan, verbose = 1L)


