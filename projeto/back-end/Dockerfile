# syntax=docker/dockerfile:1

FROM python:3.10.12-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
COPY requirements-dev.txt requirements-dev.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=painel_covid.py

EXPOSE 5000

CMD ["flask", "run"]