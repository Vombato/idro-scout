FROM debian:latest

COPY . /app

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

RUN touch data.txt

RUN pip install -r requirements.txt

CMD [ "python", "./scout.py" ]
CMD [ "python", "./exposer.py" ]
