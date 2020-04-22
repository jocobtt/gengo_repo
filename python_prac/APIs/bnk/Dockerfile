FROM python:3.7.7-buster
WORKDIR /usr/src/app

MAINTAINER jacob.braswell00@gmail.com

COPY requirements.txt ./ 

RUN pip install --no-cache-dir -r requirements

COPY . .

CMD ["python", "./script.py"] # will need to give this the path for all of my scripts maybe make them all executeable from one script?
