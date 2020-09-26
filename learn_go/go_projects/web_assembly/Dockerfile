FROM golang:1.15.2-buster 

RUN mkdir weba

RUN sudo apt-get update -y && apt install vim

COPY . . 

#RUN go get -d -v ./...
#RUN go install -v ./...

EXPOSE 8080

CMD ["weba/web-assembly"]
