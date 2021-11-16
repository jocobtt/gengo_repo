#!/bin/bash 

# install k8s cluster 

EMAIL=jacob.braswell@sas.com
RG=jabras
LOC=eastus
AKS=ocr 
DNS=ocr-jb
K8SVER=1.19

# need to work with autoscaling part for main node and for nodepools

az aks create --name $AKS \
	--resource-group $RG \
	--kubernetes-version $K8SVER \
	--dns-name-prefix $DNS \
	--load-balancer-sku standard \
	--location $LOC \
	--node-count 1 \
	--node-vm-size Standard_D4s_v3 \ # may need to check this part out 
	--nodepool-name ocr \
	--api-server-authorized-ip-ranges 149.173.0.0/16 \
	--generate-ssh-keys \
	--tags "resourceowner=$EMAIL"

az aks nodepool add \
	--resource-group $RG \
	--cluster-name $AKS \
	--name ocr-node \
	--node-count 3 \
	--mode User \
	--enable-cluster-autoscaler \
	--node-vm-size Standard_D8s_v3 \
	--node-osdisk-size 200 \
	--min-count 0 \
	--max-count 10 \
	--tags "resourceowner=$SASUID"

# get credentials for aks cluster 
az aks get-credentials --resource-group $RG --name $AKS \
	--admin -f ~/.kube/azure-config.conf
