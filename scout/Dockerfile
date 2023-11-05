FROM joyzoursky/python-chromedriver:3.9-selenium

WORKDIR /app

COPY scout.py .
COPY .env .

RUN pip install selenium python-dotenv

CMD [ "python", "-u", "scout.py" ]