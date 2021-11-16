#!/bin/bash

# will need to have kubernetes cli installed to run this script 
# here's how you can install it - 
# 

echo "input namespace name for pods we want information on"
read namespace
echo "We are assuming that your configuration file is in our ~/.kube/ location"

# i moved the file to the .kube location myself and named it jared-cluster. You can name it whatever you want and then change the name accordingly. Same with the python script. 
export KUBECONFIG=~/.kube/jared-cluster.conf

#pod_names=$(kubectl get pods -n ${namespace} -o jsonpath='{.items[*].metadata.name}')
# need to separate each line.. 


# just return the pod names in tall list
pod_names=$(kubectl get pods -n ${namespace} --no-headers -o custom-columns=':metadata.name' | cut -f2 -d '/')

echo $pod_names

