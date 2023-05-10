FROM joyzoursky/python-chromedriver:3.9-selenium

COPY . /app

WORKDIR /app

RUN touch data.txt

RUN chmod +x startup.sh

RUN pip3 install -r requirements.txt

CMD [ "./startup.sh" ]
