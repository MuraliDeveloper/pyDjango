from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, min_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=20, min_length=5,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=50, min_length=5,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    firstName = forms.CharField(label='firstName', max_length=100, min_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastName = forms.CharField(label='lastName', max_length=100, min_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

