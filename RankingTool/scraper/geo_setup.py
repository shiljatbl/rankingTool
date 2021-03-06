from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.keys import Keys
import django
from decimal import Decimal

def geo_setup(zip_code):
    options = Options()
    options.add_argument('--start-maximised')
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options)

    time.sleep(1)
    urlSearch = "https://www.Amazon.de"
    print("Setting up geolocation.")
    driver.get("https://www.Amazon.de")
    time.sleep(2)
    #setovanje ZIP code-a
    locationButton = driver.find_element_by_xpath('//*[@id="nav-global-location-slot"]/span/a')
    locationButton.click()
    time.sleep(1)
    textBox = driver.find_element_by_xpath('//*[@id="GLUXZipUpdateInput"]')
    #Unesi zeljeni ZIP
    textBox.send_keys('21266')
    time.sleep(1)
    okButton = driver.find_element_by_xpath('//*[@id="GLUXZipUpdate"]/span/input')
    time.sleep(1)
    okButton.send_keys(Keys.ENTER)
    time.sleep(1)
    driver.get("https://www.amazon.de")
    print("Geolocation setup done.")
    time.sleep(1)
    