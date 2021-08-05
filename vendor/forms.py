from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from shop.models import  Product


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=254, required=True)
    last_name = forms.CharField(max_length=254, required=True)
    email = forms.EmailField(max_length=254, help_text='Active email address')
    business_type = forms.CharField(max_length=254, required=True, help_text='e.g Electronic devices')
    business_name = forms.CharField(max_length=254, required=True, help_text='e.g Mybusiness name')
    address = forms.CharField(max_length=254, required=True, help_text='Address on business card')
    postal_code = forms.IntegerField(required=True, help_text='Postal code on business card')
    country = forms.CharField(max_length=254, required=True, help_text='Country on business card')
    website = forms.CharField(max_length=254, required=False, help_text='www.mybusiness.com')
    state = forms.CharField(max_length=254, required=True, help_text='State on business card')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','email', 'business_type', 'business_name',  'address','postal_code','state','country','website','password1', 'password2' )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'