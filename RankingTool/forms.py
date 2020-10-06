from django import forms
from .models import Product, Keyword, ScrapeProduct


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'asin',
            'sku',
            'keyword',
            'image_url',
          ]

class KeywordForm(forms.ModelForm):
    class Meta:
        model = Keyword
        fields = [
            'keyword'
        ]

class ScrapeProductForm(forms.ModelForm):
    class Meta:
        model = ScrapeProduct
        fields = [
            'product',
            'title',
            'position',
            'page',
            'rating',
            'price',
            'date'
        ]