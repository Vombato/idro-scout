from prometheus_client import start_http_server, Gauge
import time
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

LOCATION = os.environ.get("LOCATION")

# Define a Prometheus gauge metric
metric = Gauge(LOCATION, 'My metric description', ['source'])

# Start the Prometheus HTTP server
start_http_server(8001)

while True:

    # Read the last line of the data file
    with open('data.txt', 'r') as file:
        for line in file:
            pass
    
    # Split the line into two parts
    parts = line.strip().split(';')
    metric.labels(source="arpae").set(float(parts[0].strip()))

    # Wait for the HTTP server to start up
    time.sleep(10)
