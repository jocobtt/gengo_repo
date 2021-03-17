# fancier model using caret 
library(tidyverse)
library(caret)
library(DataExplorer)
set.seed(101)

df <- read.csv('http://support.sas.com/documentation/onlinedoc/viya/exampledatasets/hmeq.csv')

str(df)

# drop reason and job 
drop <- c("REASON", "JOB")
df = df[!(names(df) %in% drop)]


# deal with missing values - fill with column means 
for(i in 1:ncol(df)){
  df[is.na(df[,i]), i] <- mean(df[,i], na.rm = TRUE)
}

# partition the data 
part <- caret::createDataPartition(df$BAD, p = .75, list = FALSE)
train <- df[part,]
test <- df[-part,]


# set way we want to resample - figure out how to make this model a classification type 
fit_cont <- caret::trainControl(method = "repeatedcv",
                                number = 10,
                                repeats = 2)

gbm_fit <- train(BAD ~., 
                 data = train,
                 trControl = fit_cont,
                 verbose = TRUE)
gbm_fit