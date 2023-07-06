FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install bash

RUN python -m pip install --upgrade pip -r requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/app"

RUN pip install uwsgi

COPY uwsgi.ini .

CMD ["uwsgi", "--ini", "uwsgi.ini"]