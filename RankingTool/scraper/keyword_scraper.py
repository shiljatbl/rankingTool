from selenium import webdriver
from bs4 import BeautifulSoup
import csv
from selenium.webdriver.chrome.options import Options
import time
from RankingTool.models import Product, ScrapeProduct
from selenium.webdriver.common.keys import Keys
import django
import os


def KeywordScrape(keyword):
    productList = []

    #inicijalizacija liste stranica
    pages =[ ]

    # Setup Chromedriver-a
    options = Options()
    options.add_argument('--start-maximised')
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options)



    #zipCode = input("Please enter Zip Code:\n")
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
    #driver.get(urlSearch)
    driver.get("https://www.amazon.de")
    print("Geolocation setup done.")
    time.sleep(1)
        
    #.de za nemacku, .com za US
    urlSearch ="https://www.amazon.de/s?k="+keyword.replace(" ","+")+"&ref=nb_sb_noss_1"

    print("Retrieving data for " + keyword + "...")

    print("Retrieving data...")

    for x in range(1, 6):
        newUrl = "https://www.amazon.de/s?k=" + keyword.replace(" ", "+") + "&page=" + str(x)
        pages.append(newUrl)
    #print(pages)
    pageCounter = 1

    #print(pages)

    trigger = ""
    for p in pages:
        driver.get(p)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        #print(soup)


        try:
            trigger = soup.find("label", {"for" : "captchacharacters"}).get_text()
        except:
            trigger = "OK"

            #print("---------------------------------------------------")
            #print(trigger)
            #print("---------------------------------------------------")
        if trigger == "Zeichen eingeben":
            print("Captcha triggered. Scrape unsuccessful.")
            break



        item_tag = "s-search-result"

        result = soup.find_all("div", {
            "data-component-type": item_tag})

        for r in result:
            newProduct = ScrapeProduct()

            try:
                newProduct.asin = r.get("data-asin")
            except:
                newProduct.asin = "NoData"

            try:
                newProduct.position = str(r.get("data-index"))
            except:
                newProduct.position = "NoData"

            try:
                newProduct.page = str(pageCounter)
            except:
                newProduct.page = "NoData"
            try:
                newProduct.title = r.find("span", {"class": "a-size-base-plus a-color-base a-text-normal"}).get_text()
            except:
                newProduct.title = "NoData"
            try:
                newProduct.rating = r.find("span", {"class": "a-icon-alt"}).get_text()
            except:
                newProduct.rating ="NoData"
            try:
                #27:-7 for US
                #26:-9 za DE
                newProduct.price = str(r.find("span", {"class": "a-offscreen"}))[26:-9]

            except:
                newProduct.price = "NoData"
            try:
                newProduct.image_url = r.find("img").get("src")
            except:
                newProduct.image_url = "NoData"

            productList.append(newProduct)
        pageCounter += 1

        driver.close()
        print("Scrape done!")

        return productList



