import pandas as pd 
import numpy as np 
import os 
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import GradientBoostingClassifier 


df = pd.read_csv("hmeq.csv")

# drop the values we don't need
df = df.drop(columns = ["REASON", "Other_var"], index = 0)

# fill na w/ mean values 
df = df.fillna(df.mean())

# split test and training sets 
X = df.iloc[:,1:]
y = df.iloc[:, :1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 1010)

# create a logistic regression model 
log_mod = LogisticRegression()

log_mod.fit(X_train, y_train)

# create a decision tree model 
clf = DecisionTreeClassifier(max_leaf_node = 3, random_state = 0)
clf.fit(X_train, y_train)

# gradient boosting model 
gb = GradientBoostingClassifier(n_estimators = 100, learning_rate = .2, max_depth = 2, random_state=0)

gb.fit(X_train, y_train)

gb.score(X_test, y_test)