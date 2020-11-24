#!/bin/bash

# set up vpc network 
# create our custom vpc network 
gcloud compute networks create kubernetes-the-hard-way --subnet-mode custom 

# create our subnet - must be large enough to assign a private ip address to each node in the k8s cluster 
gcloud compute networks subnets create kubernetes \
  --network kubernetes-the-hard-way \
  --range 10.240.0.0/24

# firewall rules 
# create firewall rule that allows internal communication accross all protocols 
gcloud compute firewall-rules create kubernetes-the-hard-way-allow-internal \
  --allow tcp,udp,icmp \
  --network kubernetes-the-hard-way \
  --source-ranges 10.240.0.0/24,10.200.0.0/16

# create a firewall rule that allows external SSH, ICMP, and https
gcloud compute firewall-rules create kubernetes-the-hard-way-allow-external \
  --allow tcp:22,tcp:6443,icmp \
  --network kubernetes-the-hard-way \
  --source-ranges 0.0.0.0/0

# list the firewall rules in the k8s vpc network 
gcloud compute firewall-rules list --filter="network:kubernetes-the-hard-way"

# kubernetes pulbic ip address 
# allocate static ip address that will be attached to the external load balancer fronting the k8s api servers
gcloud compute addresses create kubernetes-the-hard-way \
  --region $(gcloud config get-value compute/region)

# verify the kubernetes-the-hard-way static ip address was created in your default compute region 
gcloud compute addresses list --filter="name=('kubernetes-the-hard-way')"


########################
# compute instances 
########################

# create 3 compute instances which will host the k8s control plane 
for i in 0 1 2; do
  gcloud compute instances create controller-${i} \
    --async \
    --boot-disk-size 200GB \
    --can-ip-forward \
    --image-family ubuntu-2004-lts \
    --image-project ubuntu-os-cloud \
    --machine-type e2-standard-2 \
    --private-network-ip 10.240.0.1${i} \
    --scopes compute-rw,storage-ro,service-management,service-control,logging-write,monitoring \
    --subnet kubernetes \
    --tags kubernetes-the-hard-way,controller
done

# create 3 compute instances which will host the k8s worker nodes 
for i in 0 1 2; do
  gcloud compute instances create worker-${i} \
    --async \
    --boot-disk-size 200GB \
    --can-ip-forward \
    --image-family ubuntu-2004-lts \
    --image-project ubuntu-os-cloud \
    --machine-type e2-standard-2 \
    --metadata pod-cidr=10.200.${i}.0/24 \
    --private-network-ip 10.240.0.2${i} \
    --scopes compute-rw,storage-ro,service-management,service-control,logging-write,monitoring \
    --subnet kubernetes \
    --tags kubernetes-the-hard-way,worker
done

# verify compute instances exist 
gcloud compute instances list --filter="tags.items=kubernetes-the-hard-way"

# configure ssh access 
echo "do the ssh configuration manually"
