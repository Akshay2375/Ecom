from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,SetPasswordForm
from django.contrib.auth.models import User
from .models import Profile
from django.db import models


class UserInfoForm(forms.ModelForm):
 
    phone=forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}) ,required=False )
    address1=forms.CharField( label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}) ,required=False )
    address2=forms.CharField( label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}) ,required=False)
    city=forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'city'}) ,required=False )
    state=forms.CharField( label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'state'}) ,required=False)
    country=forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'country'}) ,required=False )

    class Meta:
        model=Profile
        fields=( 'phone',
 'address1',
 'address2',
 'city',
  'country')
    

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),required=False)
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),required=False)
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class UpdateUserForm(UserChangeForm):
    password=None
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

class ChangePassword(SetPasswordForm):
     class Meta:
        model = User
        fields = ['new_password1','new_password2']
        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
        
        
            self.fields['new_password1'].widget.attrs['class'] = 'form-control'
            self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['new_password1'].label = ''
            self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
            
            self.fields['new_password2'].widget.attrs['class'] = 'form-control'
            self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
            self.fields['new_password2'].label = ''
            self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'