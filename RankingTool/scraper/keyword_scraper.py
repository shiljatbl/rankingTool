from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time
from RankingTool.models import Product, ScrapeProduct, Keyword, KeywordCrawl, Marketplace
from selenium.webdriver.common.keys import Keys
import django
from decimal import Decimal
import datetime

def KeywordScrape(keyword):
    
    

    

    #inicijalizacija liste proizvoda
    productList = []

    #inicijalizacija liste stranica
    pages =[]

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
    driver.get("https://www.amazon.de")
    print("Geolocation setup done.")
    time.sleep(1)
        
    #.de za nemacku, .com za US
    urlSearch ="https://www.amazon.de/s?k="+keyword.replace(" ","+")+"&ref=nb_sb_noss_1"

    print("Retrieving data for " + keyword + "...")

    print("Retrieving data...")

    try:
        crawl_keyword = Keyword.objects.get(keyword=keyword)
                    
    except:
        crawl_keyword = Keyword(keyword=keyword)
        crawl_keyword.save()
    marketplace = Marketplace.objects.get(name="Amazon.de")
    crawl = KeywordCrawl.objects.create( date=datetime.datetime.now(), keyword=crawl_keyword, marketplace=marketplace)
    
       
    for page in range(1, 3):
        newUrl = "https://www.amazon.de/s?k=" + keyword.replace(" ", "+") + "&page=" + str(page)
        pages.append(newUrl)
    
    pageCounter = 1
    for p in pages:
        driver.get(p)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        item_tag = "s-search-result"

        result = soup.find_all("div", {"data-component-type": item_tag })
        page_position = 1
        for r in result:
            # in the search result div the class named "AdHolder" is used for sponsored products
            amazon_ad = r.get('class')
            if not 'AdHolder' in amazon_ad:
                newScrapeProduct = ScrapeProduct()
                try:
                    new_asin = r.get("data-asin")
                except:
                    new_asin = "NoData"
                
                try:
                    newProduct = Product.objects.get(asin=new_asin)
                except:
                    newProduct = Product.objects.create(asin=new_asin)
                
                try:
                    newScrapeProduct.position = page_position
                except:
                    newScrapeProduct.position = 999
                
                try:
                    newScrapeProduct.page = str(pageCounter)
                except:
                    newScrapeProduct.page = 999
                
                try:
                    newScrapeProduct.title = r.find("span", {"class": "a-text-normal"}).get_text()
                except:
                    newScrapeProduct.title = "NoData"
                
                try:
                    newScrapeProduct.rating = Decimal(r.find("span", {"class": "a-icon-alt"}).get_text().split()[0].replace(',', '.'))
                except:
                    newScrapeProduct.rating = 0.0
                
                try:
                    #27:-7 for US
                    #26:-9 za DE
                    new_price = str(r.find("span", {"class": "a-offscreen"}))[26:-9]
                    newScrapeProduct.price = Decimal(new_price.replace(',', '.'))
                except:
                    newScrapeProduct.price = 0
                
                try:
                    newProduct.image_url = r.find("img").get("src")
                except:
                    newProduct.image_url = "NoData"
                
                try:
                    new_keyword = Keyword.objects.get(keyword=keyword)
                    
                except:
                    new_keyword = Keyword(keyword=keyword)
                    new_keyword.save()

                newScrapeProduct.date = datetime.datetime.now()
            
                newProduct.keyword.add(new_keyword)
                newScrapeProduct.keyword = new_keyword
                newScrapeProduct.product = newProduct
                newProduct.save()
                newScrapeProduct.save()
                
                
                
                crawl.products.add(newScrapeProduct)
                productList.append(newScrapeProduct)
                page_position += 1
        pageCounter += 1

    driver.close()
    print("Scrape done!")

    return productList



