#this below is if I want to run terraform on its own from an image
FROM hashicorp/terraform:light

LABEL maintainer "Jacob Braswell"

COPY . /terraform/ 


ENTRYPOINT ["bash"]


# If I want to build my own terraform image from scratch 
#FROM golang:alpine
#MAINTAINER "HashiCorp Terraform Team <terraform@hashicorp.com>"

#ENV TERRAFORM_VERSION=0.10.0

#RUN apk add --update git bash openssh

#ENV TF_DEV=true
#ENV TF_RELEASE=true

#WORKDIR $GOPATH/src/github.com/hashicorp/terraform
#RUN git clone https://github.com/hashicorp/terraform.git ./ && \
    git checkout v${TERRAFORM_VERSION} && \
    /bin/bash scripts/build.sh

#WORKDIR $GOPATH
#ENTRYPOINT ["terraform"]
