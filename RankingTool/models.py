from django.db import models
from django.urls import reverse
from datetime import datetime
# Create your models here.

class Keyword(models.Model):
    keyword = models.CharField(max_length=200,default="")
    
    def __str__(self):
        return self.keyword


class Product(models.Model):
    asin = models.CharField(max_length=10, default="")
    sku = models.CharField(max_length=200,default="")
    keyword = models.ManyToManyField(Keyword)
    image_url = models.CharField(max_length=200,default="")
    tracked_product = models.BooleanField(default=False)
    
    @property
    def latest_update(self):
        
        try:
            latest_scrape = ScrapeProduct.objects.filter(product__asin=self.asin).order_by('-date')[0]
            latest_date = latest_scrape.date
        except:
            latest_date = 0
        
        return latest_date
    

    def __str__(self):
        return self.asin

    def get_absolute_url(self): # new
        return reverse('product', args=[str(self.id)])



    
class ScrapeProduct(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=200,default="-")
    position = models.IntegerField(default=0)
    page = models.IntegerField(default=0)
    rating = models.DecimalField(default=0, max_digits=2, decimal_places=1)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.product.asin

    def get_absolute_url(self): # new
        return reverse('scrape-product', args=[str(self.id)])