#!/bin/bash
# download prometheus 
curl -L https://github.com/prometheus/prometheus/releases/download/v2.18.0/prometheus-2.18.0.${platform}-amd64.tar.gz

# unzip tarball - find a way to make this variable come from the above info so i don't have a change to ruin it
tar -xzf prometheus-2.18.0.${platform}-amd64.tar.gz

# cd into directory
cd prometheus-2.18.0.${platform}-amd64

# make changes I want to make to prometheus.yaml file
