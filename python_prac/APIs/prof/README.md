# Introduction

We are working on a machine learning system that predicts male or female based
on three input variables:
- Height
- Weight
- Shoe size

A data scientist, working seperately from you, has created a machine learning model
in the form of a serialized/pickled file called "a_model.joblib"

You don't need to know how this file was produced, but only that you can load the model
from disk and pass it height/weight/shoesize to get a prediciton.  If you are curious, you can look
at the train_model.py to see how the file was created.

An example of how to load the model and call it is in the run_model.py file.

## Your task - Create 3 things

1) Create an HTTP/Web API for this model.   This would generally be done using Flask
or FastAPI

2) Package up your REST api in a docker container, using a Dockerfile to build the container

3) Describe (or draw) how you might deploy this API/docker container on AWS.  Assume
this is a high volume and critical part of our systems and must have high availability.
This does NOT need to be fancy.  A photo of a hand-drawn diagram is just fine.

## Your submission

Send back to proofpoint
1) Your complete python code solution for the REST api
2) Your dockerfile that packages your code as a container
3) Your description (or drawing) of how you would deploy this system.
