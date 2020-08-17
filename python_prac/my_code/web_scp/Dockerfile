FROM ubuntu:latest

RUN apt-get update && apt-get -y update 

RUN apt-get install -y build-essential python3-pip python3-dev 


RUN mkdir -p src/scrape
WORKDIR src/scrape
COPY . bs4-rent.py

RUN pip3 install -r requirements.txt


RUN cd $PWD

#CMD ["python3", "run", "scrape.py"]
