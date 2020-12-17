from product_app.models import Product
from django import forms

class ProductForm(forms.ModelForm):
    product_details=forms.CharField(widget=forms.Textarea)
    class Meta():
        model = Product
        exclude = ['product_reviews']