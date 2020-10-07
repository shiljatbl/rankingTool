from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product, ScrapeProduct, Keyword
from .forms import ProductForm, KeywordForm, ScrapeProductForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse
from .scraper.product_scraper import ProductScraper 
from .scraper.keyword_scraper import KeywordScrape
from decimal import Decimal
from django.http import Http404

def scraper(request, keyword):
    
    context = {
        "keyword": keyword
    }
    

    return render(request, "scraper.html", context)

def scraper_home(request):
    
    context = {}

    if request.method == 'POST':
        keyword = request.POST.get('keyword')


        product_list = KeywordScrape(keyword)
        
        for product in product_list:
            new_product = product
            new_product.save()


        context = {
            'products': product_list,
            'keyword': keyword,
        }

        return render(request, "scraper_keyword.html", context)
    
    return render(request, "scraper_home.html", context)



def scraper_keyword(request, keyword):
    product_list = KeywordScrape(keyword)
    
    for product in product_list:
            new_product = product
            new_product.save()

    context = {
        'products': product_list,
        'keyword': keyword,
    }

    return render(request, "scraper_keyword.html", context)
    
   
def product_list_view(request):
    products = Product.objects.filter(tracked_product=True)
    context = {
        'products': products
    }

    return render(request, "product/product_list.html", context)

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

def product_detail(request, id):
    
    product = get_object_or_404(Product, pk=id)
    keyword_list = Keyword.objects.filter(product__pk=id)
    
    
    scraped_data = ScrapeProduct.objects.filter(product__pk=id).order_by('-date')

    context = {
        'product': product,
        'scraped_data': scraped_data,
        'keywords': keyword_list,
        
    }
    return render(request, 'product/product_detail.html', context)

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

# ScrapeProduct Views

class ScrapeProductsView(ListView):
    queryset = ScrapeProduct.objects.all()
    template_name = 'scrape_product/scrape_product_list.html'


class ScrapeProductCreateView(CreateView):
    form_class = ScrapeProductForm
    queryset = ScrapeProduct.objects.all()
    template_name = 'scrape_product/scrape_product_create.html'

class ScrapeProductDetailView(DetailView):
    queryset = ScrapeProduct.objects.all()
    template_name = 'scrape_product/scrape_product_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(ScrapeProduct, id=id_)

class ScrapeProductUpdateView(UpdateView):
    template_name = 'scrape_product/scrape_product_create.html'
    form_class = ScrapeProductForm
    queryset = ScrapeProduct.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(ScrapeProduct, id=id_)


class ScrapeProductDeleteView(DeleteView):
    template_name = 'scrape_product/scrape_product_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(ScrapeProduct, id=id_)

    def get_success_url(self):
        return reverse('scrape-product-list')





