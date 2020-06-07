FROM python:latest

COPY requirements.txt ./

RUN apt-get update && /
    apt-get install curl

CMD ["

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . . 

CMD [ "python", "./
