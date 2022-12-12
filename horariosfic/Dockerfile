FROM python:3.9.6-slim-buster

WORKDIR /servicios

RUN apt-get update && \
    apt-get install -y libpq-dev gcc

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD [ "./services_init.sh" ]