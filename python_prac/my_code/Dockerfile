FROM python:latest

RUN mkdir /my_code 
WORKDIR /my_code

COPY *.py /my_code

RUN apt-get update \
	&& apt-get install vim -y 

RUN pip install -y requirements.txt
