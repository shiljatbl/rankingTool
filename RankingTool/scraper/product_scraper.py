from selenium import webdriver
from bs4 import BeautifulSoup
import csv
from selenium.webdriver.chrome.options import Options
import time
import geolocation
from RankingTool.models import Product
import django
import os

def ProductScraper(asin):
    #Setup Chromedriver-a
    options = Options()
    options.add_argument('--start-maximised')
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options)
    url = "https://www.amazon.de/dp/" + asin
    driver.get(url)
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    try:
        result = soup.find("span", { "id": "productTitle"}).get_text()
    except:
        result = "No Data"

    return result