#!/bin/bash

# apply the yaml file
kubectl apply -f shpod-create.yaml

# change to correct namespace 
kubectl config set-context --current --namespace=kube-course

# list resources available in kube-course namespace
kubectl get all

# kubectl execute into shell
kubectl attach --namespace=kube-course -ti shpod

