from prometheus_client import start_http_server, Gauge
import time
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

NUMBER = os.environ.get("LOCATIONS")
LOCATIONS = []
DBS = []
METRICS = []

for n in range(1, int(NUMBER)+1):
    location = os.environ.get("LOCATION_" + str(n))
    print("Adding location " + str(n) + " " + location)
    LOCATIONS.append(location)
    print(LOCATIONS)
    DBS.append("db/data" + str(n)  + ".txt")
    print(DBS)
    METRICS.append(Gauge(location, 'Livello idrometrico ' + location, ['source']))


# Start the Prometheus HTTP server
start_http_server(8001)

while True:

    try:

        for n in range(1, int(NUMBER)+1):
            # Read the last line of the data file
            with open(DBS[n-1], 'r') as file:
                for line in file:
                    pass
        
            # Split the line into two parts
            parts = line.strip().split(';')
            METRICS[n-1].labels(source="arpae").set(float(parts[0].strip()))
    except Exception as e:
        print("Error: " + str(e))
    
    # Wait for the HTTP server to start up
    time.sleep(10)
