from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product, ScrapeProduct, Keyword, KeywordCrawl, Settings
from .forms import ProductForm, KeywordForm, ScrapeProductForm, SettingsForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse
from .scraper.product_scraper import ProductScraper 
from .scraper.keyword_scraper import KeywordScrape
from .scraper.multiple_keyword_scraper import KeywordScrapeMultiple
from decimal import Decimal
from django.http import Http404
from django.core.paginator import Paginator
import csv
import codecs

def scraper(request, keyword):
    
    context = {
        "keyword": keyword
    }
    

    return render(request, "scraper.html", context)

def scraper_home(request):
    
    no_of_keywords = len(Keyword.objects.all())
    no_of_products = len(Product.objects.all())
    no_of_tracked_products = len(Product.objects.filter(tracked_product=True))
    no_of_scrapes = len(KeywordCrawl.objects.all())

    context = {
        'no_of_keywords': no_of_keywords,
        'no_of_products': no_of_products,
        'no_of_tracked_products': no_of_tracked_products,
        'no_of_scrapes': no_of_scrapes
    }



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
    products = Product.objects.all()
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'products': products,
        'page_obj': page_obj
    }

    return render(request, "product/product_list.html", context)


def tracked_product_list_view(request):
    #products = Product.objects.all()
    products = Product.objects.filter(tracked_product=True)
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': products,
        'page_obj': page_obj
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



# Keyword Views

def keyword_list_view(request):
    #products = Product.objects.all()
    keywords = Keyword.objects.all().order_by('-keyword')
    
    context = {
        'keywords': keywords
    }

    return render(request, "keyword/keyword_list.html", context)


def keyword_list_amazon_de(request):
    keywords = Keyword.objects.filter(marketplace__name='Amazon.de').order_by('-keyword')

    context = {
        'keywords': keywords
    }

    return render(request, "keyword/keyword_list.html", context)

def keyword_list_amazon_fr(request):
    keywords = Keyword.objects.filter(marketplace__name='Amazon.fr').order_by('-keyword')

    context = {
        'keywords': keywords
    }

    return render(request, "keyword/keyword_list.html", context)

def keyword_list_amazon_it(request):
    keywords = Keyword.objects.filter(marketplace__name='Amazon.fr').order_by('-keyword')

    context = {
        'keywords': keywords
    }

    return render(request, "keyword/keyword_list.html", context)

def keyword_list_ebay_de(request):
    keywords = Keyword.objects.filter(marketplace__name='eBay.de').order_by('-keyword')

    context = {
        'keywords': keywords
    }

    return render(request, "keyword/keyword_list.html", context)

class KeywordCreateView(CreateView):
    form_class = KeywordForm
    queryset = Keyword.objects.all()
    template_name = 'keyword/keyword_create.html'

def keyword_detail(request, id):
    
    keyword = get_object_or_404(Keyword, pk=id)
    
    
    crawls = KeywordCrawl.objects.filter(keyword__pk=id).order_by('-date')
    scraped_data = ScrapeProduct.objects.filter(keyword__pk=id).order_by('-date')

    if len(scraped_data) == 0:
        keyword_image_url = "-"
    else:
        keyword_image_url = scraped_data[len(scraped_data)-1].product.image_url

    context = {
        'keyword': keyword,
        'scraped_data': scraped_data,
        'image_url': keyword_image_url,
        'crawls': crawls,
        
        
    }
    return render(request, 'keyword/keyword_detail.html', context)

class KeywordUpdateView(UpdateView):
    template_name = 'keyword/keyword_create.html'
    form_class = KeywordForm
    queryset = Keyword.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Keyword, id=id_)


class KeywordDeleteView(DeleteView):
    template_name = 'keyword/keyword_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Keyword, id=id_)

    def get_success_url(self):
        return reverse('keyword-list')



# Crawl Views

def crawl_list_view(request):
    
    crawls = KeywordCrawl.objects.all().order_by('-date')
    context = {
        'crawls': crawls
    }

    return render(request, "crawl/crawl_list.html", context)




def crawl_detail(request, id):
    
    crawl = get_object_or_404(KeywordCrawl, pk=id)
    products = crawl.products.all()

    

    context = {
        'crawl': crawl,
        'products': products
        
        
    }
    return render(request, 'crawl/crawl_detail.html', context)



class CrawlDeleteView(DeleteView):
    template_name = 'crawl/crawl_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(KeywordCrawl, id=id_)

    def get_success_url(self):
        return reverse('crawl-list')


def crawl_download(request):

    
    crawls = KeywordCrawl.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="downloadTest.csv"'

    writer = csv.writer(response, delimiter=',')

    writer.writerow(['keyword', 'marketplace', 'date', 'asin', 'title', 'price', 'page', 'position', 'rating', 'image_url'])

    for crawl in crawls:
        
        for scraped_product in crawl.products.all():
            writer.writerow([crawl.keyword.keyword, crawl.marketplace.name, crawl.date, scraped_product.product.asin, scraped_product.title, scraped_product.price, scraped_product.page, scraped_product.position, scraped_product.rating, scraped_product.product.image_url])

    return response

def crawl_single_download(request, id):

    crawl = get_object_or_404(KeywordCrawl, pk=id)


    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="' + crawl.keyword.keyword + "-" + str(crawl.date) + '.csv"'

    response.write(codecs.BOM_UTF8)
    writer = csv.writer(response, delimiter=',')

    writer.writerow(['keyword', 'marketplace', 'date', 'asin', 'title', 'price', 'page', 'position', 'rating', 'image_url'])

    for scraped_product in crawl.products.all():
        writer.writerow([crawl.keyword.keyword, crawl.marketplace.name, crawl.date, scraped_product.product.asin, scraped_product.title, scraped_product.price, scraped_product.page, scraped_product.position, scraped_product.rating, scraped_product.product.image_url])

    return response

class SettingsUpdateView(UpdateView):
    template_name = 'settings/settings_create.html'
    form_class = SettingsForm
    queryset = Settings.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Settings, id=id_)

def scrape_all_keywords(response):
    #keywords = Keyword.objects.all()
    KeywordScrapeMultiple()

    return redirect('/crawl/')

def delete_all_scrapeProducts(response):

    ScrapeProduct.objects.all().delete()
    Product.objects.all().delete()
    Keyword.objects.all().delete()
    KeywordCrawl.objects.all().delete()


    return redirect('/crawl/')