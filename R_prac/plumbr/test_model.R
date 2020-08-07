# create a simple model 
# https://github.com/blairj09-talks/bmdd-plumber
# https://github.com/rstudio/rsconnect

library('datasets')

df <- datasets::airquality


# try a regression model 
mod = lm(Ozone ~ . , data = df)

saveRDS(mod, here::here("R", "plumbr", "air.rds"))

