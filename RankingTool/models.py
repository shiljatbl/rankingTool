from django.db import models
from django.urls import reverse
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

    
