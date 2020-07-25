FROM python:3.7-slim

RUN apt-get update && apt-get install -y --no-install-recommends build-essential locales-all

ADD requirements.txt /

RUN pip install -r requirements.txt

WORKDIR /usr/src/app

COPY . .

EXPOSE 8000
