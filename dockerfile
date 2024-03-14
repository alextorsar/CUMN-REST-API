FROM python:3.13.0a4-alpine3.19

WORKDIR /app

COPY ./ /app/

RUN apk update && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev zlib-dev jpeg-dev && pip install --upgrade pip && pip install psycopg2

RUN python -m pip install -r requirements.txt