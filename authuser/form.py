from django import forms
import django
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm

from album.models import User

class MyUserCreationForm(UserCreationForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Your Name'
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Username'
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
        'class':'form-control',
        'placeholder':'Email'
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'placeholder':'Password'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'placeholder':'Confirm Password'
        }
    ))

    class Meta:
        model = User
        fields = ['name','username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','avatar']