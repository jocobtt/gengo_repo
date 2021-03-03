# ensemble models 
library(caret)
library(tidyverse)
library(quadprog)

# http://www.mlfactor.com/ensemble.html#stacked-ensembles

err_pen_train <- predict(fit_pen_pred, x_penalized_train) - training_sample$R1M_Usd  # Reg.
err_tree_train <- predict(fit_tree, training_sample) - training_sample$R1M_Usd       # Tree
err_RF_train <- predict(fit_RF, training_sample) - training_sample$R1M_Usd           # RF
err_XGB_train <- predict(fit_xgb, train_matrix_xgb) - training_sample$R1M_Usd        # XGBoost
err_NN_train <- predict(model, NN_train_features) - training_sample$R1M_Usd          # NN
E <- cbind(err_pen_train, err_tree_train, err_RF_train, err_XGB_train, err_NN_train) # E matrix
colnames(E) <- c("Pen_reg", "Tree", "RF", "XGB", "NN")                               # Names
cor(E)                 

apply(abs(E), 2, mean) # Mean absolute error or columns of E 

w_ensemble <- solve(t(E) %*% E) %*% rep(1,5)                             # Optimal weights
w_ensemble <- w_ensemble / sum(w_ensemble)
w_ensemble

err_pen_test <- predict(fit_pen_pred, x_penalized_test) - testing_sample$R1M_Usd     # Reg.
err_tree_test <- predict(fit_tree, testing_sample) - testing_sample$R1M_Usd          # Tree
err_RF_test <- predict(fit_RF, testing_sample) - testing_sample$R1M_Usd              # RF
err_XGB_test <- predict(fit_xgb, xgb_test) - testing_sample$R1M_Usd                  # XGBoost
err_NN_test <- predict(model, NN_test_features) - testing_sample$R1M_Usd             # NN
E_test <- cbind(err_pen_test, err_tree_test, err_RF_test, err_XGB_test, err_NN_test) # E matrix
colnames(E_test) <- c("Pen_reg", "Tree", "RF", "XGB", "NN")
apply(abs(E_test), 2, mean)             # Mean absolute error or columns of E 

err_EW_test <- apply(E_test, 1, mean)  # Equally weighted combination
mean(abs(err_EW_test))

err_opt_test <- E_test %*% w_ensemble   # Optimal unconstrained combination
mean(abs(err_opt_test))