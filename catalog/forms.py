from django import forms

from django import forms
from .models import Product

class ProductFilterForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, label='Название')
    min_price = forms.DecimalField(max_digits=10, decimal_places=2, required=False, label='Минимальная цена')
    max_price = forms.DecimalField(max_digits=10, decimal_places=2, required=False, label='Максимальная цена')
    clothing_type = forms.ChoiceField(choices=[('', 'Любой')] + Product.TYPE_CHOICES[:-6], required=False, label='Тип товара')
    accessories_type = forms.ChoiceField(choices=[('', 'Любой')] + Product.TYPE_CHOICES[-6:], required=False, label='Тип товара')

    def __init__(self, *args, **kwargs):
        super(ProductFilterForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название'})
        self.fields['min_price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Минимальная цена'})
        self.fields['max_price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Максимальная цена'})
        self.fields['clothing_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['accessories_type'].widget.attrs.update({'class': 'form-control'})