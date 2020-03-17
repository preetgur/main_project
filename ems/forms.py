from ems.models import Register_Employee
from django.forms import ModelForm
from django import forms


class Register_Emp_Form(forms.ModelForm):
    
    class Meta:
        model = Register_Employee
        fields = "__all__"


# create user form

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class User_Form(UserCreationForm):

    class Meta :
        model = User
        fields = ['username','email','password1','password2']

#You can change the 'id' and 'name' of fields here
        widgets ={
            'username' : forms.TextInput(attrs = {'class':'form-control','placeholder':'Username','id':'user'}),


        }