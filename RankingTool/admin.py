from django.contrib import admin

from .models import Product, Keyword, ScrapeProduct, KeywordCrawl

admin.site.register(Product)
admin.site.register(Keyword)
admin.site.register(ScrapeProduct)
admin.site.register(KeywordCrawl)
# Register your models here.
