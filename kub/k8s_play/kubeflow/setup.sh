#! /bin/bash


# set up istio 

#download istio into current directory
curl -L https://istio.io/downloadIstio | sh -

# change directories into isto directory
cd istio-1.5.2

# set path for istioctl 
export PATH=$PWD/bin:$PATH

# add the helm repo for istio if I don't already have it
helm repo add istio.io https://storage.googleapis.com/istio-release/releases/1.5.2/charts

# create istio-system namespace
kubectl create ns istio-system

# install istio crd 
helm template install/kubernetes/helm/istio-init --name istio-init --namespace istio-system | kubectl apply -f - 

# run minimal configuration profile
helm template install/kubernetes/helm/istio --name istio --namespace istio-system \
  --values install/kubernetes/helm/istio/values-istio-minimal.yaml | kubectl apply -f - 

# set the namespace kubectl is in to be istio-system
kubectl config set-context --current --namespace=istio-system

# kubectl label namespace default istio-injection=enabled

# get tarball for kfctl
curl -L https://github.com/kubeflow/kfctl/releases/download/v1.0.2/kfctl_v1.0.2-0-ga476281_${platform}.tar.gz --output tar_kfctl.tar.gz
tar -xvf tar_kfctl.tar.gz

# set path for kfctl
export PATH=$PATH:${KF_PATH}

# set KF_NAME 
export ${KF_NAME}

# set path to base directory where we will store kubeflow deployments - in this case we will use the working directory 
export BASE_DIR=$PWD 
export KF_DIR=$PWD

# make directory for kubeflow - just one below our current working directory
cd ${KF_DIR}

# apply our kfctl_istio install file
kfctl apply -V -f kfctl_k8s_istio.v1.0.2.yaml

# make sure it all worked 
kubectl get all -n kubeflow

# port forward kubeflow so it can be used
kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80
