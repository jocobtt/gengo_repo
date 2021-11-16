#!/bin/bash

NAMESPACE=sas-pub 

kubectl get ns ${NAMESPACE} -o json > ${NAMESPACE}.json

# edit out finalizer having kubernetes portion 
sed '16d' ${NAMESPACE}.json

# executing cleanup command 
kubectl replace --raw "/api/v1/namespaces/${NAMESPACE}/finalize" -f ${NAMESPACE}.json 
