from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegisterForm(UserCreationForm):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
