# Use the official Python image
FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y libpq-dev musl-dev build-essential python3-dev python3-psycopg2 postgis

RUN mkdir /code
WORKDIR /code
ADD ./ /code/


RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "AccuKnox_Practical.wsgi", "--bind", "0.0.0.0:8000"]