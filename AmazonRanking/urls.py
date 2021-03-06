"""AmazonRanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from RankingTool import views as rankingToolViews
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from RankingTool.views import ProductDeleteView, ProductsView, ProductCreateView, ProductDetailView, ProductUpdateView, product_detail, product_list_view, tracked_product_list_view
from RankingTool.views import ScrapeProductDeleteView, ScrapeProductsView, ScrapeProductCreateView, ScrapeProductDetailView, ScrapeProductUpdateView
from RankingTool.views import KeywordDeleteView, KeywordCreateView, keyword_detail, KeywordUpdateView, keyword_list_view, keyword_list_amazon_de, keyword_list_amazon_fr, keyword_list_amazon_it, keyword_list_ebay_de
from RankingTool.views import CrawlDeleteView, crawl_detail, crawl_list_view
from RankingTool.views import crawl_download, crawl_single_download
from RankingTool.views import SettingsUpdateView, scrape_all_keywords, delete_all_scrapeProducts


urlpatterns = [
    
    path('admin/', admin.site.urls, name="admin"),
    #path('product/<int:id>', ProductDetailView.as_view(), name="product"),
    path('product/<int:id>', rankingToolViews.product_detail, name="product"),
    path('product/create/', ProductCreateView.as_view(), name="product-create"),
    path('product/<int:id>/delete/', ProductDeleteView.as_view(), name="product-delete"),
    path('product/', rankingToolViews.product_list_view, name="product-list"),
    path('product/<int:id>/update/', ProductUpdateView.as_view(), name="product-update"),
    path('product2/<int:id>', rankingToolViews.product_detail, name="product2"),
    path('product/tracked/', rankingToolViews.tracked_product_list_view, name="tracked-product-list"),
    
    path('keyword/scrape/', rankingToolViews.scraper_home, name="scraper-keyword-home"),
    path('keyword/scrape/<str:keyword>', rankingToolViews.scraper_keyword, name="scraper-keyword"),
    
    path('scrape-product/<int:id>', ScrapeProductDetailView.as_view(), name="scrape-product"),
    path('scrape-product/create/', ScrapeProductCreateView.as_view(), name="scrape-product-create"),
    path('scrape-product/<int:id>/delete/', ScrapeProductDeleteView.as_view(), name="scrape-product-delete"),
    path('scrape-product/', ScrapeProductsView.as_view(), name="scrape-product-list"),
    path('scrape-product/<int:id>/update/', ScrapeProductUpdateView.as_view(), name="scrape-product-update"),
    #path('scraper/<str:asin>', rankingToolViews.scraper, name="scraper-product"),

    path('keyword/', keyword_list_view, name="keyword-list"),
    path('keyword/amazon/de/', keyword_list_amazon_de, name="keyword-list-de"),
    path('keyword/amazon/fr/', keyword_list_amazon_fr, name="keyword-list-fr"),
    path('keyword/amazon/it/', keyword_list_amazon_it, name="keyword-list-it"),
    path('keyword/ebay/de/', keyword_list_ebay_de, name="keyword-list-ebay-de"),

    path('keyword/<int:id>', keyword_detail, name="keyword-detail"),
    path('keyword/create/', KeywordCreateView.as_view(), name="keyword-create"),
    path('keyword/<int:id>/delete/', KeywordDeleteView.as_view(), name="keyword-delete"),
    path('keyword/<int:id>/update/', KeywordUpdateView.as_view(), name="keyword-update"),

    path('crawl/', crawl_list_view, name="crawl-list"),
    path('crawl/<int:id>', crawl_detail, name="crawl-detail"),
    path('crawl/<int:id>/delete/', CrawlDeleteView.as_view(), name="crawl-delete"),
    
    path('download-csv/', crawl_download, name='download'),
    path('download-csv/<int:id>', crawl_single_download, name='single-download'),
    
    path('settings/', SettingsUpdateView.as_view(), name='settings' ),

    path('keyword-scrape/', scrape_all_keywords, name='scrape-all-keywords'),

    path('delete/', delete_all_scrapeProducts, name='delete'),
    path('', rankingToolViews.scraper_home, name="home")
]

urlpatterns += staticfiles_urlpatterns()