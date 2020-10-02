from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse
from .scraper.product_scraper import ProductScraper 




def scraper(request, asin):
    title = ProductScraper(asin)
    context = {
        'title': title
    }
    

    return render(request, "scraper.html", context)


class ProductsView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/product_list.html'


class ProductCreateView(CreateView):
    form_class = ProductForm
    queryset = Product.objects.all()
    template_name = 'product/product_create.html'

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/product_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Product, id=id_)

class ProductUpdateView(UpdateView):
    template_name = 'product/product_create.html'
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





