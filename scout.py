import time
from datetime import datetime
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

URL = os.environ.get("URL")
URL_SUFFIX = os.environ.get("URL_SUFFIX")
LOCATION = os.environ.get("LOCATION")

URL_SUFFIX = os.environ.get("URL_SUFFIX")
LOCATION = os.environ.get("LOCATION")



# Set up headless browser with Chrome driver

time_old = ""
while True:
    try:
        print ("Scraping...")
        url = URL + datetime.now().strftime("%Y-%m-%d") + URL_SUFFIX
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)

        # Navigate to webpage and wait for JavaScript to load
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ultDato')))

        data = driver.find_element(By.CLASS_NAME, 'ultDato').text
        time_now = driver.find_element(By.CLASS_NAME, 'ultOre').text

        # Close browser
        driver.quit()
        
        # If time_now contains " locale" remove it
        if " locale" in time_now:
            time_now = time_now.replace(" locale", "")
        if " m" in data:
            data = data.replace(" m", "")
        # Close browser
        driver.quit()
        
        # If time_now contains " locale" remove it
        if " locale" in time_now:
            time_now = time_now.replace(" locale", "")
        if " m" in data:
            data = data.replace(" m", "")

        if time_now != time_old:
            print ("New data found!")
            print(data + " | " + time_now)
            with open("data.txt", "a") as file:
                file.write(data + ";" + time_now + "\n")
        else:
            print("No new data")
        time_old = time_now
    except Exception as e:
        print("Error: " + str(e))
    
    print("Waiting 2 minutes...")
    time.sleep(120)
