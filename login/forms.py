from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class UserForm(ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Userlogin
        fields = '__all__'
        # fields = '__all__' same as before shows all fields of table

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

