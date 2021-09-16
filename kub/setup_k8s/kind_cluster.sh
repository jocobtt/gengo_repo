#!/bin/bash

OS=darwin


# install kind 
#brew install kind
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.10.0/kind-${OS}-amd64
chmod +x ./kind
mv ./kind /usr/local/bin

# set up kind cluster 
kind create cluster --name cka 