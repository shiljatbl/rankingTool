from django.contrib import admin

from .models import Product, Keyword, ScrapeProduct, KeywordCrawl, Marketplace

admin.site.register(Product)
admin.site.register(Keyword)
admin.site.register(ScrapeProduct)
admin.site.register(KeywordCrawl)
admin.site.register(Marketplace)
# Register your models here.
