from django.contrib import admin

from .models import Product, Keyword, ScrapeProduct, KeywordCrawl, Marketplace, Settings

admin.site.register(Product)
admin.site.register(Keyword)
admin.site.register(ScrapeProduct)
admin.site.register(KeywordCrawl)
admin.site.register(Marketplace)
admin.site.register(Settings)
# Register your models here.
