FROM python:latest

RUN mkdir /my_code 
WORKDIR /my_code

COPY . /my_code

RUN apt-get update \
	&& apt-get install vim -y 
