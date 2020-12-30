from django import forms
from django.contrib.auth.models import User
from App1.models import UserInfo, Product



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
        exclude = ['seller']
