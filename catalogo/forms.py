from django import forms
from .models import Customer, Category, Product, Sale, SaleItem

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'birth_date', 'nummber_phone', 'identification_card']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type', 'brand', 'operating_system']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'amount', 'category', 'picture']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer', 'date', 'total_price']

from django.forms import inlineformset_factory

SaleProductFormSet = inlineformset_factory(Sale, SaleItem, fields=('product', 'quantity', 'price'))
