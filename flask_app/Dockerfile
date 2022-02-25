FROM python:3.8

WORKDIR usr/src/flask_app
COPY requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends \
    unixodbc-dev \
    unixodbc \
    libpq-dev \
    vim
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install psycopg2
RUN pip install gunicorn

COPY . .


