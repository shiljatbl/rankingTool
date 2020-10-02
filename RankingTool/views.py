from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

from selenium import webdriver
from bs4 import BeautifulSoup
import csv
from selenium.webdriver.chrome.options import Options
import time
import geolocation
from RankingTool.models import Product
import django
import os






def scraper(request, asin):

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
    result = soup.find("span", { "id": "productTitle"}).get_text()

    context =  {
        "title": result
    }

    return render(request, "scraper.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        "form": form
    }
    return render (request, "product/products_create.html", context)


def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "object": obj
    }
    return render (request, "product/detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id = id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../')
    context = {
        "object": obj
    }
    return render(request, "product/product_delete.html", context)

def product_list(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "product/product_list.html", context)

# def product_update_view(request)
