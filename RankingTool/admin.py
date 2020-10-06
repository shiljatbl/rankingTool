from django.contrib import admin

from .models import Product, Keyword, ScrapeProduct

admin.site.register(Product)
admin.site.register(Keyword)
admin.site.register(ScrapeProduct)
# Register your models here.
