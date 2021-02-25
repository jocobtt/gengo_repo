FROM rstudio/r-base:4.0-bionic

COPY . . 

RUN install2.r -s remotes
COPY DESCRIPTION /pkg/DESCRIPTION
RUN Rscript -e "remotes::install_deps(pkgdir = '/pkg/', dependencies=TRUE, upgrade = 'always', force = FALSE, quiet = FALSE)"

