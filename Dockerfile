FROM python:3.7-slim

RUN apt-get update && apt-get install -y --no-install-recommends build-essential locales-all

ADD requirements.txt /

RUN pip install -r requirements.txt

WORKDIR /usr/src/app

COPY . .

EXPOSE 8000

ENV SECRET_KEY = "+6^1!pyr55exgnez0ci*&g^d@hbt9!lh@=(cdg-%5(d+^%5tx-", DJANGO_DEBUG = ''
