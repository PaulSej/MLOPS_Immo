# syntax=docker/dockerfile:1

FROM python:3.13-slim

WORKDIR /flask-api

COPY linear_regression_apartments_paris.pkl linear_regression_apartments_paris.pkl
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
#EXPOSE 5000

CMD ["python", "./api.py"]
