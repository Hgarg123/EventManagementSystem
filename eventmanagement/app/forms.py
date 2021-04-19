from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordChangeForm

username_validator = UnicodeUsernameValidator()


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['password']


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=20, min_length=4, required=True, help_text='Required: Username',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    name = forms.CharField(max_length=20, min_length=4, required=True, help_text='Required: First Name',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}))
    mobile_no = forms.CharField(max_length=10, min_length=10, required=True, help_text='Required: Number',
                           widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}))
    email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.',
                             widget=(forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Email'})))
    password1 = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(
                                    attrs={'class': 'form-control','placeholder': 'Enter Password'})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Password Confirmation'), widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Enter Confirm Password'}),
                                help_text=_('Just Enter the same password, for confirmation'))

    class Meta:
        model = User
        fields = ( 'username' ,'mobile_no' , 'name', 'email', 'password1', 'password2')

class MyChangeFormPassword(PasswordChangeForm):
    pass

