# reference this https://hackernoon.com/machine-learning-w22g322x and this https://runnable.com/docker/python/dockerize-your-flask-application
from flask import render_template, request, jsonify
import flask
import numpy as np 
import traceback
import pickle 
import pandas as pd 

app = Flask(__name__, template_folder='templates')

# import our pickled model 
with open('webapp/model/model.pkl', 'rb') as f:
  classifier = pickle.load (f)

with open('webapp/model/model_columns.pkl', 'rb') as f:
  model_columns = pickle.load (f)

@app.route('/')
def welcome():
  return "Something about my model"

@app.route('/predict', methods=['POST','GET'])
def predict(): 
