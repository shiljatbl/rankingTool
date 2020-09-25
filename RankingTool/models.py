from django.db import models

# Create your models here.

class Product(models.Model):
    asin = models.CharField(max_length=10, default="Test")
    title = models.CharField(max_length=200,default="Test")
    price = models.FloatField(default=0.0)
    position = models.IntegerField(default=0)
    page = models.IntegerField(default=0)




    def __str__(self):
        return self.asin



