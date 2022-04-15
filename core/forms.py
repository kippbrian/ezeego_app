from dataclasses import fields
from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length='50')
    last_name=forms.CharField(max_length='50')
    email=forms.EmailField(max_length='100')
    phone=forms.CharField(max_length='20')
    
    class Meta:
        model=User
        fields=('first_name','last_name','email','phone','password1','password2')
        
    def clean_email(self):
        email=self.cleaned_data['email'].lower()
        if User.objects.filter(email=email):
            raise ValidationError('This email address already exists')
        return email