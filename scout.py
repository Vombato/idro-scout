import time
from datetime import datetime
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

URL = os.environ.get("URL")

NUMBER = os.environ.get("LOCATIONS")

LOCATIONS = []
URL_LOCATIONS = []
DBS = []
CACHE = []

URL_MIDDLE = os.environ.get("URL_MIDDLE")
URL_STAZIONE = os.environ.get("URL_STAZIONE")
URL_SUFFIX = os.environ.get("URL_SUFFIX")

# add to LOCATIONS and DBS lists the locations and data files


for n in range(1, int(NUMBER)+1):
    print("Adding location " + str(n))
    LOCATIONS.append(os.environ.get("LOCATION_" + str(n)))
    URL_LOCATIONS.append(os.environ.get("URL_LOCATION_" + str(n)))
    DBS.append("db/data" + str(n)  + ".txt")
    CACHE.append("")

print("LOCATIONS: " + str(LOCATIONS))
print("URL_LOCATIONS: " + str(URL_LOCATIONS))
print("DBS: " + str(DBS))


# Set up headless browser with Chrome driver

while True:
    for n in range(1, int(NUMBER)+1):
        try:
            today = datetime.now()
            past3 = today - timedelta(days=3)
            print ("Scraping " + LOCATIONS[n-1] + "...")
            url = URL + URL_LOCATIONS[n-1] + URL_MIDDLE + past3.strftime("%Y-%m-%d") + "/" + datetime.now().strftime("%Y-%m-%d") + URL_STAZIONE + URL_LOCATIONS[n-1] + URL_SUFFIX
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            driver = webdriver.Chrome(options=chrome_options)
            # Navigate to webpage and wait for JavaScript to load
            print("Navigating to " + url)
            driver.get(url)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ultDato')))
            data = driver.find_element(By.CLASS_NAME, 'ultDato').text
            print("Data: " + data)
            time_now = driver.find_element(By.CLASS_NAME, 'ultOre').text
            print("Time: " + time_now)
            # Close browser
            driver.quit()
            
            # If time_now contains " locale" remove it
            if " locale" in time_now:
                time_now = time_now.replace(" locale", "")
            if " m" in data:
                data = data.replace(" m", "")

            if time_now != CACHE[n-1] or time_now == "":
                print ("New data found!")
                print(data + " | " + time_now)
                with open(DBS[n-1], "a") as file:
                    file.write(data + ";" + time_now + "\n")
            else:
                print("No new data")
            CACHE[n-1] = time_now
    
        except Exception as e:
            print("Error: " + str(e))
    
    print("Waiting 2 minutes...")
    time.sleep(120)
