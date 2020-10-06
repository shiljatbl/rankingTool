from django.db import models
from django.urls import reverse
from datetime import datetime
# Create your models here.

class Keyword(models.Model):
    keyword = models.CharField(max_length=200,default="-")
    
    def __str__(self):
        return self.keyword


class Product(models.Model):
    asin = models.CharField(max_length=10, default="-")
    sku = models.CharField(max_length=200,default="-")
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200,default="-")



    def __str__(self):
        return self.asin

    def get_absolute_url(self): # new
        return reverse('product', args=[str(self.id)])



    
class ScrapeProduct(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,default="-")
    position = models.IntegerField(default=0)
    page = models.IntegerField(default=0)
    rating = models.CharField(max_length=200,default="-")
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.asin

    def get_absolute_url(self): # new
        return reverse('scrape-product', args=[str(self.id)])