FROM debian:latest

COPY . /app

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y wget python3 python3-pip python3-dev

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN apt-get install -y ./google-chrome-stable_current_amd64.deb

RUN touch data.txt

RUN chmod +x startup.sh

RUN pip3 install -r requirements.txt

CMD [ "./startup.sh" ]
