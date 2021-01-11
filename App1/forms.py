from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from App1.models import UserInfo, Product, CartItem, Order



class UserForm(forms.ModelForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your first name','class' : 'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your last name', 'class' : 'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your password', 'class' : 'form-control'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your password', 'class' : 'form-control'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your username', 'class' : 'form-control'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter your email','class' : 'form-control'}))
    class Meta():
        model = User
        fields = ('first_name','last_name','email','username', 'password')




#To create radiobutton introduce widget outside meta class
options = (('buyer', 'Buyer Account'), ('seller', 'Seller Account'))
class UserInfoForm(forms.ModelForm):
    BuyerOrSeller = forms.ChoiceField(choices = options, widget = forms.RadioSelect(), label = "Select the type of account:")

    class Meta():
        model = UserInfo
        fields = ('BuyerOrSeller',)


class ProductForm (forms.ModelForm):
    details = forms.CharField(widget=forms.Textarea)
    class Meta ():
        model = Product
        exclude = ['seller','favourites','views']


currency_choices = (('$','$'),('€','€'),('L.E','L.E'))
payment_choices = (('cod','COD(Cash on delivery)'),('credit','Credit Card'))
choose = (('yes','Yes'),('no','No'))
class OrderForm (forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'governorate, city, street, building, apartment', 'class':'form-control', 'id':'address'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'phone number','class':'form-control', 'id':'phone'}))
    zip_code = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'zip code','class':'form-control', 'id':'zip'}))
    currency = forms.ChoiceField(choices=currency_choices, widget = forms.RadioSelect(), label = "Choose the currency you want to pay with:")
    payment_method = forms.ChoiceField(choices=payment_choices, widget = forms.RadioSelect(), label = "Choose your payment method:")
    discount_points = forms.ChoiceField(choices=choose, widget = forms.RadioSelect(), label = "Do you want to use your discount points?")
    class Meta():
        model = Order
        fields = ('address', 'phone_number', 'zip_code', 'currency', 'payment_method', 'discount_points')