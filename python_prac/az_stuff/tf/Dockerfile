# syntax=docker/dockerfile:experimental
ARG TERRAFORM_VERSION=0.13.4
ARG AZURECLI_VERSION=2.14.2
ARG BRANCH=main

FROM hashicorp/terraform:$TERRAFORM_VERSION as terraform
FROM mcr.microsoft.com/azure-cli:$AZURECLI_VERSION
ARG KUBECTL_VERSION=1.18.8

COPY --from=terraform /bin/terraform /bin/terraform

WORKDIR /viya4-iac-azure

RUN apk --update --no-cache add git openssh \
  && curl -sLO https://storage.googleapis.com/kubernetes-release/release/v$KUBECTL_VERSION/bin/linux/amd64/kubectl \
  && chmod 755 ./kubectl \
  && mv ./kubectl /usr/local/bin/kubectl

ARG TIMESTAMP

RUN git clone --single-branch $BRANCH "https://github.com/sassoftware/viya4-iac-azure.git" /viya4-iac-azure \
  && terraform init /viya4-iac-azure

ENTRYPOINT ["/bin/terraform"]
