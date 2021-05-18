#!/bin/bash

WRKDIR=$(realpath .)

VIYA_DIR=${WRKDIR}/deploy/
echo "VIYA_DIR: " ${VIYA_DIR}

GHOST_DIR=${WRKDIR}/cluster-setup/ghosts
echo "GHOST_DIR: " ${GHOST_DIR}

NGINX_DIR=${WRKDIR}/cluster-setup/nginx
echo "NGINX_DIR: " ${NGINX_DIR}

LDAP_DIR=${WRKDIR}/cluster-setup/ldap 
echo "LDAP_DIR: " ${LDAP_DIR}

INGRESS_DIR=${WRKDIR}/cluster-setup/nginx

# install go if it isn't already there...

# clear docker system to free up ports for our load balancer etc. 
yes | sudo docker system prune 

# install kind 
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.9.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind


# our cluster config to apply to our cluster - 5 worker nodes 
cat << 'EOF' > kind_worker.yaml 
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
    image: kindest/node:v1.18.8@sha256:f4bcc97a0ad6e7abaf3f643d890add7efe6ee4ab90baeb374b4f41a4c95567eb
    kubeadmConfigPatches:
    - |
      kind: InitConfiguration
      nodeRegistration:
        kubeletExtraArgs:
         node-labels: "ingress-ready=true"
    extraPortMappings:
    - containerPort: 80
      hostPort: 80
      protocol: TCP
    - containerPort: 443
      hostPort: 443
      protocol: TCP
  - role: worker
    image: kindest/node:v1.18.8@sha256:f4bcc97a0ad6e7abaf3f643d890add7efe6ee4ab90baeb374b4f41a4c95567eb
  - role: worker
    image: kindest/node:v1.18.8@sha256:f4bcc97a0ad6e7abaf3f643d890add7efe6ee4ab90baeb374b4f41a4c95567eb
  - role: worker 
    image: kindest/node:v1.18.8@sha256:f4bcc97a0ad6e7abaf3f643d890add7efe6ee4ab90baeb374b4f41a4c95567eb
  - role: worker 
    image: kindest/node:v1.18.8@sha256:f4bcc97a0ad6e7abaf3f643d890add7efe6ee4ab90baeb374b4f41a4c95567eb
  # see if we only need 4 workers 
EOF

# create our cluster 
kind create cluster --name test --config kind_worker.yaml --kubeconfig $HOME/.kube/config
# try building with this image next --image=registry.unx.sas.com/micamp/kindest/node:v1.19.7 espeically given the dockerfile I have. 
# kind create cluster --name ghost --config kind-cluster.yaml --kubeonfig $HOME/.kube/config --image=registry.unx.sas.com/micamp/kindest/node:v1.19.7

# check to see if we have connection to kind cluster 
kubectl get nodes 

# taint a node for cas 
#kubectl taint nodes test-worker workload.sas.com/class=cas:NoSchedule


# can either do nginx for localhost 

# install nginx controller - just need localhost 
cd ${INGRESS_DIR} || exit
kustomize build . | kubectl apply -f - 

# setup openldap 
cd ${LDAP_DIR} || exit
kustomize build . | kubectl apply -f - 

# set up ghost postgresql database 
kubectl create ns ghosts
cd $GHOST_DIR  || exit
kustomize build . | kubectl apply -f - 


# create nfs-server 
kubectl create ns nfs-server

helm repo add stable https://charts.helm.sh/stable

# will need to find a replacement for this as it is deprecated 
helm install nfs-server-provisioner stable/nfs-server-provisioner -n nfs-server --set presistence.enabled=true,persistence.size=50Gi


# create viya4 namespace 
kubectl create ns gpu-viya

#echo "Go apply your kustomization.yaml file at ${VIYA_DIR} and then run 'kustomize build . | kubectl apply -f -'"
# apply kustomize manifest for viya deployment - need to find way to set ip for dns to load balancer ip 
cd ${VIYA_DIR} || exit
kustomize build . | kubectl apply -f - 

