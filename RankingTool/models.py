from django.db import models

# Create your models here.

class Product(models.Model):
    asin = models.CharField(max_length=10)

    def __str__(self):
        return self.asin



