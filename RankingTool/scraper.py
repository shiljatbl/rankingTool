from selenium import webdriver
from bs4 import BeautifulSoup
import csv
from selenium.webdriver.chrome.options import Options
import time
import geolocation
from models import Product



productList = []

#inicijalizacija liste stranica
pages =[ ]

#Setup Chromedriver-a
options = Options()
options.add_argument('--start-maximised')
#options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=options)

GeoLocation.set_location()

#keyword koji ce biti pretrazivan
keyword = input("Please enter keywords:\n")


#.de za nemacku, .com za US
urlSearch ="https://www.amazon.de/s?k="+keyword.replace(" ","+")+"&ref=nb_sb_noss_1"

print("Retrieving data for " + keyword + "...")

print("Retrieving data...")

for x in range(1, 11):
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
        newProduct = Product()

        try:
            newProduct.asin = r.get("data-asin")
        except:
            newProduct.asin = "NoData"

        try:
            newProduct.position = str(r.get("data-index"))
        except:
            newProduct.asin = "NoData"

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

if not trigger == "Zeichen eingeben":
    print("Scraping done!")
    time.sleep(1)
    print("Saving data to CSV/rankingDE.csv")

    with open("CSV/rankingDE.csv", mode="w", newline="\n", encoding="utf-8") as crawledFile:
        amazonWriter = csv.writer(crawledFile, delimiter=";", quoting=csv.QUOTE_MINIMAL)

        amazonWriter.writerow(["Page", "Position", "ASIN", "Title", "Price", "Rating", "ImageLink"])

        for p in productList:
            amazonWriter.writerow([p.page, p.position, p.asin, p.title, p.price, p.rating, p.image_url])

    print("Scrape done successful. CSV saved.")
