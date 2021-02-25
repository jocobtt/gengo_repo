# Build simple model from mtcars dataset
setwd("~/model_ops/mmgr/retrain_r/plumber/")
## ---- cars-model
# Model ---- (insert fancy model here)
cars_model <- lm(mpg ~ cyl + hp,
                 data = mtcars)

# Save model ----
saveRDS(cars_model, here::here("R", "model-api", "cars-model.rds"))

