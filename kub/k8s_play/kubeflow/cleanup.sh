#!/bin/bash
cd ${KF_DIR}
kfctl delete -f kfctl_k8s_istio.v1.0.2.yaml

# delete namespace
kubectl delete ns kubeflow 

# delete kubeflow resources - is this what I want though? 
rm -rf kustomize 
rm -rf .cache 

# delete istio stuff 

# cd into istio directory
cd ~/Downloads/istio-1.5.2/

# remove helm template for now 
helm template install/kubernetes/helm/istio --name istio --namespace istio-system \
  --values install/kubernetes/helm/istio/values-istio-minimal.yaml | kubectl delete -f - 

# delete istio-system namespace
kubectl delete namespace istio-system 

# move namespace context uses back to kube-prac (namespace I use)
kubectl config set-context --current --namespace=kube-prac

# remove istio directory
rm -rf istio-1.5.2

