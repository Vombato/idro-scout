from prometheus_client import start_http_server, Gauge
import time
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

LOCATION = os.environ.get("LOCATION")

# Define a Prometheus gauge metric
metric = Gauge(LOCATION + "_m", 'My metric description', ['time'])

# Start the Prometheus HTTP server
start_http_server(8001)

# Read the data from the file
with open('data.txt', 'r') as f:
    data = f.readlines()

# Loop through the data and update the metric
for line in data:
    parts = line.strip().split(';')
    metric.labels(time=parts[1].strip()).set(float(parts[0].strip()))

# Wait for the HTTP server to start up
time.sleep(1)

# Keep the script running
while True:
    time.sleep(1)