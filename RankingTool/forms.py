from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'asin',
            'price',
            'position',
            'page',
            'image_url',
            'rating',
            'title'

        ]
