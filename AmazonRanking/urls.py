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
from pages import views
from RankingTool import views as rankingToolViews
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from RankingTool.views import ProductDeleteView, ProductsView, ProductCreateView, ProductDetailView, ProductUpdateView, product_detail
from RankingTool.views import ScrapeProductDeleteView, ScrapeProductsView, ScrapeProductCreateView, ScrapeProductDetailView, ScrapeProductUpdateView

urlpatterns = [
    path('', views.home_view, name="home"),
    path('admin/', admin.site.urls, name="admin"),
    #path('product/<int:id>', ProductDetailView.as_view(), name="product"),
    path('product/<int:id>', rankingToolViews.product_detail, name="product"),
    path('product/create/', ProductCreateView.as_view(), name="product-create"),
    path('product/<int:id>/delete/', ProductDeleteView.as_view(), name="product-delete"),
    path('product/', ProductsView.as_view(), name="product-list"),
    path('product/<int:id>/update/', ProductUpdateView.as_view(), name="product-update"),
    path('product2/<int:id>', rankingToolViews.product_detail, name="product2"),
    path('keyword/', rankingToolViews.scraper_home, name="keyword"),
    path('keyword/<str:keyword>', rankingToolViews.scraper_keyword, name="scraper-keyword"),
    path('scrape-product/<int:id>', ScrapeProductDetailView.as_view(), name="scrape-product"),
    path('scrape-product/create/', ScrapeProductCreateView.as_view(), name="scrape-product-create"),
    path('scrape-product/<int:id>/delete/', ScrapeProductDeleteView.as_view(), name="scrape-product-delete"),
    path('scrape-product/', ScrapeProductsView.as_view(), name="scrape-product-list"),
    path('scrape-product/<int:id>/update/', ScrapeProductUpdateView.as_view(), name="scrape-product-update"),
    #path('scraper/<str:asin>', rankingToolViews.scraper, name="scraper-product"),
    
    
]

urlpatterns += staticfiles_urlpatterns()