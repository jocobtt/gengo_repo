#!/bin/bash
# https://grafana.com/docs/loki/latest/installation/helm/
# set up grafana helm chart
kubectl create ns loki 
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

# helm loki
helm upgrade --install loki --namespace=loki grafana/loki-stack --set grafana.enabled=true,prometheus.enabled=true,prometheus.alertmanager.persistentVolume.enabled=false,prometheus.server.persistentVolume.enabled=false,loki.persistence.enabled=true,loki.persistence.storageClassName=azurefile,loki.persistence.size=5Gi

# install grafana
# helm install loki-grafana grafana/grafana

# get grafana password
kubectl get secret --namespace loki loki-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo

# port forward dashboard 
kubectl port-forward -n loki svc/loki-grafana 3000:80

# http/readiness probe is failing...

# reach it at localhost:3000