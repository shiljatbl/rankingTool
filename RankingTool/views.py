from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm, KeywordForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse
from .scraper.product_scraper import ProductScraper 
from .scraper.keyword_scraper import KeywordScrape



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
        
        context = {
            'products': product_list,
            'keyword': keyword,
        }

        return render(request, "scraper_keyword.html", context)
    
    return render(request, "scraper_home.html", context)



def scraper_keyword(request, keyword):
    #KeywordScrape(keyword)
    
    
    context = {
        'keyword': keyword
    }
    return render(request, "scraper_keyword.html", context)



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





