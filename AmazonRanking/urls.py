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

from RankingTool.views import product_detail_view, product_create_view, product_delete_view, product_list, ProductsView, ProductCreateView

urlpatterns = [
    path('', views.home_view, name="home"),
    path('admin/', admin.site.urls),
    path('product/<int:id>', product_detail_view, name="product"),
    path('product/create/', ProductCreateView.as_view(), name="product-create"),
    path('scraper/', rankingToolViews.scraper, name="scraper"),
    path('scraper/<str:asin>', rankingToolViews.scraper, name="scraper-product"),
    path('product/<int:id>/delete/', product_delete_view, name="delete-product"),
    path('product/', ProductsView.as_view(), name="product-list"),
    
    
]

urlpatterns += staticfiles_urlpatterns()