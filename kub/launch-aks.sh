#!/bin/bash

# examples/doc - 
# https://denniszielke.medium.com/fully-private-aks-clusters-without-any-public-ips-finally-7f5688411184
# https://m-suryaprakash95.medium.com/different-ways-to-connect-to-private-aks-cluster-azure-kubernetes-service-ff4921227027
# https://blog.baeke.info/2021/07/01/dns-options-for-private-azure-kubernetes-service/
# https://docs.microsoft.com/en-us/azure/aks/private-clusters


base=rockpoint

EMAIL=christine.jackson@sas.com

DNS=${base}

RG=${base}-dep-rg
RG2=${base}-dep-hub

LOC=canadacentral

AKS=${base}-aks

K8SVER=1.20.7

SASDNS=jabras.unx.sas.com

# create groups 
#az group create -n $RG -l $LOC

# create our virtual network 
az network vnet create -n ${base}-vnet-kube -g $RG --address-prefixes 10.100.0.0/16

# create hub network 
az network vnet create -n ${base}-vnet-hub -g ${RG2} --address-prefix 10.100.2.0/16

# create subnets and peer the ones we need to peer 
az network vnet subnet create -g ${RG2} --vnet-name ${base}-vnet-hub -n ${base}-sub-hub-fw --address 10.100.2.0/24

az network vnet subnet create -g ${RG2} --vnet-name ${base}-vnet-hub -n ${base}-sub-hub-jump --address 10.100.2.1/24

az network vnet subnet create -g ${RG} --vnet-name ${base}-vnet-kube -n ${base}-sub-kube-ing --address 10.100.0.0/24

az network vnet subnet create -g ${RG} --vnet-name ${base}-vnet-kube -n ${base}-kube-vnet --address 10.100.0.1/24

az network vnet peering create -g $RG2 -n HubToSpoke1 --vnet-name ${base}-vnet-hub --remote-vnet ${base}-vnet-kube --allow-vnet-access
az network vnet peering create -g $RG2 -n Spoke1ToHub --vnet-name ${base}-vnet-kube--remote-vnet ${base}-vnet-hub --allow-vnet-access

# get subnet id so we can associate the vnet with our aks cluster 
az network vnet subnet list -g $RG --vnet-name ${base}-vnet-kube -o json --query "[].id"


# create user assigned identity in rg 
az identity create --name private-aks-iden --resource-group $RG

# create our role w/ principal id 
az role assignment create --role Contributor --assignee --scope "/subscriptions/7c9431b4-e713-4355-996a-3d6c37b24e7b/resourcegroups/${RG}"



# create the cluster 
az aks create --name $AKS \
     --resource-group $RG \
     --kubernetes-version $K8SVER \
     --dns-name-prefix $DNS  \
     --load-balancer-sku standard \
     --enable-private-cluster \
     --location $LOC \
     --node-count 2 \
     --node-vm-size Standard_D8s_v4 \
     --nodepool-name system \
     --node-osdisk-size 200 \
     --docker-bridge-address 172.17.0.1/16 \
     --service-cidr 192.168.0.0/16 \
     --dns-service-ip 192.168.0.10 \
     --vnet-subnet-id "/subscriptions/7c9431b4-e713-4355-996a-3d6c37b24e7b/resourceGroups/${RG}/providers/Microsoft.Network/virtualNetworks/azuse-itadmin-test-vpn-vnet/subnets/azuse-itadmin-test-subnet" \
     --enable-managed-identity \
     --assign-identity "/subscriptions/7c9431b4-e713-4355-996a-3d6c37b24e7b/resourcegroups/azuse-itadmin-test-vpn-rg/providers/Microsoft.ManagedIdentity/userAssignedIdentities/pemcne-test-aks" \
     --network-plugin azure \ # could try kubenet
     --outbound-type userDefinedRouting \
     --tags "resourceowner=$EMAIL" 


# add nodepool

az aks nodepool add \
  --resource-group $RG \
  --cluster-name $AKS \
  --name cas \
  --node-count 3 \
  --mode User \
  --enable-cluster-autoscaler \
  --node-vm-size Standard_E8ds_v4 \
  --node-osdisk-size 200 \
  --min-count 3 \
  --max-count 5 \
  --node-taints "workload.sas.com/class=cas:NoSchedule" \
  --tags "resourceowner=$EMAIL"

az aks nodepool add \
  --resource-group $RG \
  --cluster-name $AKS \
  --name stateful \
  --node-count 1 \
  --mode User \
  --enable-cluster-autoscaler \
  --node-vm-size Standard_E16ds_v4 \
  --node-osdisk-size 200 \
  --min-count 1 \
  --max-count 3 \
  --node-taints "workload.sas.com/class=stateful:NoSchedule", "workload.sas.com/class=stateless:NoSchedule" \
  --node-labels 
  --tags "resourceowner=$EMAIL"

az aks nodepool add \
  --resource-group $RG \
  --cluster-name $AKS \
  --name connect \
  --node-count 3 \
  --mode User \
  --enable-cluster-autoscaler \
  --node-vm-size Standard_E2ds_v4 \
  --node-osdisk-size 200 \
  --min-count 3 \
  --max-count 5 \
  --node-taints "workload.sas.com/class=stateless:NoSchedule" \
  --tags "resourceowner=$EMAIL"

az aks nodepool add \
  --resource-group $RG \
  --cluster-name $AKS \
  --name compute \
  --node-count 1 \
  --mode User \
  --enable-cluster-autoscaler \
  --node-vm-size Standard_E4-2ds_v4 \
  --node-osdisk-size 200 \
  --min-count 1 \
  --max-count 5 \
  --node-taints "workload.sas.com/class=compute:NoSchedule" \
  --tags "resourceowner=$EMAIL"

# get credentials for the aks cluster 
az aks get-credentials --resource-group $RG --name $AKS \
  --admin -f ~/.kube/azure-config.conf

export KUBECONFIG=~/.kube/azure-config.conf

#test to make sure it worked 
kubectl get nodes 
