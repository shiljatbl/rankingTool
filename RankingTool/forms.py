from django import forms
from .models import Product, Keyword


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