from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse
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


class ProductsView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/product_list.html'


class ProductCreateView(CreateView):
    form_class = ProductForm
    queryset = Product.objects.all()
    template_name = 'product/products_create.html'

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Product, id=id_)

class ProductUpdateView(UpdateView):
    template_name = 'product/products_create.html'
    form_class = ProductForm
    queryset = Product.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Product, id=id_)


class ProductDeleteView(DeleteView):
    template_name = 'product/product_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Product, id=id_)

    def get_success_url(self):
        return reverse('product-list')





