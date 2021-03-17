# build decision tree model and save it as rds value 
iris_mod <- tree::tree(Species ~ . ,data = iris)

# save the model 
saveRDS(iris_mod, "iris-model.rds")
saveRDS(iris_mod, here::here("R", "model-api", "iris-model.rds"))
