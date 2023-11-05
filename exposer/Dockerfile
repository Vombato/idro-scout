FROM python:3.9.18-alpine

WORKDIR /app

COPY exposer.py .

EXPOSE 8001

RUN pip install prometheus-client python-dotenv

CMD [ "python", "-u", "exposer.py" ]