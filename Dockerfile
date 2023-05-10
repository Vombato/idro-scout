FROM joyzoursky/python-chromedriver:3.9-selenium

RUN touch data.txt

RUN chmod +x startup.sh

RUN pip3 install -r requirements.txt

CMD [ "./startup.sh" ]
