#!/bin/bash

#download istio into current directory
curl -L https://istio.io/downloadIstio | sh -

# change directories into isto directory
cd istio-1.5.2

# set path for istioctl 
export PATH=$PWD/bin:$PATH

# add the helm repo for istio if I don't already have it
helm repo add istio.io https://storage.googleapis.com/istio-release/releases/1.5.2/charts

# create istio-system namespace
kubectl create ns istio-system

# install istio crd 
helm template install/kubernetes/helm/istio-init --name istio-init --namespace istio-system | kubectl apply -f - 

# run minimal configuration profile
helm template install/kubernetes/helm/istio --name istio --namespace istio-system \
  --values install/kubernetes/helm/istio/values-istio-minimal.yaml | kubectl apply -f - 

# set the namespace kubectl is in to be istio-system
kubectl config set-context --current --namespace=istio-system

# kubectl label namespace default istio-injection=enabled
