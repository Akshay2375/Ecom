from django import forms
from .models import ShippingAdress


class Shippingform(forms.ModelForm):
    shipping_full_name=forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'full_name'}) ,required=False)
    shipping_address1=forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address1'}) ,required=False)
    shipping_address2=forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address2'}) ,required=False)
    shipping_email=forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}) ,required=False)
    shipping_city=forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'city'}) ,required=False)
    
    
    class Meta:
        model=ShippingAdress
        fields='__all__'
        exclude=['user',]
        
        
        
class PaymentForm(forms.Form):
    card_number=forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'card Number'}) ,required=False)
    card_name=forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'card name'}) ,required=False) 
    card_address=forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'card adrress'}) ,required=False)
    card_city=forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'card city'}) ,required=False)