FROM debian:latest

COPY . /app

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev

RUN touch data.txt

RUN pip3 install -r requirements.txt

CMD [ "./startup.sh" ]
