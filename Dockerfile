FROM python:3.9

COPY . /app

WORKDIR /app

RUN touch data.txt

RUN pip install -r requirements.txt

CMD [ "python", "./scout.py" ]
CMD [ "python", "./exposer.py" ]
