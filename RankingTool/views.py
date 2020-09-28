from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

def scraper(request):
    return render(request, "scraper.html", {})


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        "form": form
    }
    return render (request, "product/products_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        "object": obj
    }
    return render (request, "product/detail.html", context)