FROM python:3.11.8-bookworm

WORKDIR /app

COPY ./ /app/

#RUN apt install gcc musl-dev postgresql-dev python3-dev libffi-dev zlib-dev jpeg-dev openssl-dev && pip install --upgrade pip && pip install psycopg2

RUN python -m pip install -r requirements.txt