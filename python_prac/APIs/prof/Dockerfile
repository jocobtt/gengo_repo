FROM python:3.10-slim as builder 

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"


RUN mkdir /work
WORKDIR /work
COPY requirements.txt requirements.txt
COPY run_model.py run_model.py
COPY train_model.py train_model.py
COPY a_model.joblib a_model.joblib

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

# final stage 
FROM python:3.10-slim
COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /work /work
WORKDIR /work

ENV PATH="/opt/venv/bin:$PATH"
CMD ["python3", "run_model.py"]
