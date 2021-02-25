FROM trestletech/plumber

# install packages needed 
RUN r -e 'install.packages(c("randomForest"))'

# copy resources needed 
RUN mkdir /data 
COPY model.Rdata /data
COPY api.R /data
WORKDIR /data

EXPOSE 8000
ENTRYPOINT ["R", "-e", \
	"pr <- plumber::plumb('/data/api.R'); pr$run(host='0.0.0.0', port=8000)"]
