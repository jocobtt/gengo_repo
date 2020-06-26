#!/bin/bash

# download helm - need to test this out first though
platform=darwin
HELMVERS=3.1.2
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
rm get_helm.sh

kubectl create serviceaccount --namespace kube-system tiller
kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
helm init --service-account tiller

# add bitnami chart
helm repo add softonic https://charts.softonic.io

helm install softonic/knative-serving -name knative-test --version 2.0.1
