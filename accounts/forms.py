from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms


# Inherit from built in "UserCreationForm"
class Register_Form(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

