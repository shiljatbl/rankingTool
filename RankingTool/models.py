from django.db import models
from django.urls import reverse
from datetime import datetime
# Create your models here.




class Product(models.Model):
    asin = models.CharField(max_length=10, default="Test")
    sku = models.CharField(max_length=200,default="Test")
    keyword = models.CharField(max_length=200,default="Test")
    image_url = models.CharField(max_length=200,default="Test")



    def __str__(self):
        return self.asin

    def get_absolute_url(self): # new
        return reverse('product', args=[str(self.id)])

class Keyword(models.Model):
    keyword = models.CharField(max_length=200,default="Test")
    
    def __str__(self):
        return self.keyword

    
class ScrapeProduct(models.Model):
    asin = models.CharField(max_length=10, default="Test")
    keyword = models.CharField(max_length=200,default="Test")
    image_url = models.CharField(max_length=200,default="Test")
    title = models.CharField(max_length=200,default="Test")
    position = models.IntegerField(default=0)
    page = models.IntegerField(default=0)
    rating = models.CharField(max_length=200,default="Test")
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.asin

    def get_absolute_url(self): # new
        return reverse('scrape-product', args=[str(self.id)])