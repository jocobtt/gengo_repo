FROM python:3

RUN pip install flask

RUN mkdir -p /test/app
WORKDIR /test/app
COPY main.py .
ENV FLASK_APP=/test/app/main.py

ENV APP_NAME=jabras.app

CMD ["flask", "run", "--host=0.0.0.0"]
