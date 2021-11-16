#!/bin/bash

NS=viya
export KUBECONFIG="~/.kube/gtp-config.config"

pod_names=$(kubectl get pods -n ${NS} --no-headers -o custom-columns=':metadata.name' | cut -f2 -d '/')

kubectl logs -l app=sassoftware #? 

for pod in pod_names:
    pod_logs=$(kubectl logs -n ${NS} $pod)
    