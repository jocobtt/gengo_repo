FROM ubuntu:18.04

RUN sudo apt-get update && apt-get -y update 

RUN apt-get install -y build-essential python3-pip python3-dev 

RUN mkdir -p src/sms

WORKDIR src/sms

COPY . . 

RUN pip3 install -r requirements.txt

CMD ["python3", "run", "send_sms.py"]
