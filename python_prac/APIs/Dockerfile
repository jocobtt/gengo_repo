FROM ubuntu:latest

MAINTAINER Jacob Braswell 

RUN apt-get update && apt-get install -y python3 python3-dev python3-pip nginx 

# copy the requirements for our app
COPY ./requirements.txt

RUN mkdir -p /test/app
WORKDIR /test/app
COPY main.py .
ENV FLASK_APP=/test/app/main.py

ENV APP_NAME=jabras.app

RUN pip3 install -r requirements.txt

ENTRYPOINT["python3"]

CMD ["flask", "run", "--host=0.0.0.0"]
