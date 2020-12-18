from django import forms
from django.contrib.auth.models import User
from App1.models import UserInfo, Product
from colorfield.fields import ColorField



class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'password')



#To create radiobutton introduce widget outside meta class
options = (('buyer', 'Buyer Account'), ('seller', 'Seller Account'))
class UserInfoForm(forms.ModelForm):
    BuyerOrSeller = forms.ChoiceField(choices = options, widget = forms.RadioSelect(), label = "Select the type of account:")

    class Meta():
        model = UserInfo
        fields = ('BuyerOrSeller',)


type = (('shirt', 'Shirt'), ('trousers', 'Trousers'), ('dess', 'Dress'), ('skirt', 'Skirt'));
class ProductForm (forms.ModelForm):
    product_type = forms.ChoiceField(label = "Product Type:", choices = type)
    in_stock = forms.IntegerField(label = "In stock:")
    price = forms.DecimalField(label = "Price")
    picture = forms.ImageField(label = "Image", required = False)
    class Meta ():
        model = Product
        fields = ('product_type', 'in_stock', 'price', 'Color', 'picture')
