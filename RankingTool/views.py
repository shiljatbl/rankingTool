from django.shortcuts import render, get_object_or_404, redirect
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