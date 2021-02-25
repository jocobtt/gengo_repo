FROM rocker/verse:3.6.1 

ARG DEBIAN_FRONTEND=noninteractive 

COPY . . 

RUN apt-get update 

RUN install2.r -s remotes 
COPY DESCRIPTION /pkg/DESCRIPTION
RUN Rscript -e "remotes::install_deps(pkgdir = '/pkg/', dependencies=TRUE, upgrade = 'always', force = FALSE, quiet = FALSE)"

 
