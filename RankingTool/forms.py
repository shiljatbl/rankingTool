from django import forms
from .models import Product, Keyword, ScrapeProduct, Settings


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'asin',
            'sku',
            'keyword',
            'image_url',
            'tracked_product'
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
            'date',
            'keyword'
        ]


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = [
            'zip_code',
            'no_of_pages'
          ]