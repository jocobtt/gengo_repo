FROM ubuntu:18.04

RUN apt-get update && apt-get -y update 

RUN apt-get install -y build-essential python3-pip python3-dev 


RUN mkdir -p src/scrape
WORKDIR src/scrape
COPY . . 

#RUN pip3 install -r requirements.txt

RUN pip3 install googlemaps

RUN pip3 install pandas 

RUN pip3 install bs4 

RUN pip3 install requests


RUN cd $PWD

#CMD ["python3", "run", "scrape.py"]
