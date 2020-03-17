from django.db import models

# Create your models here.

class Register_Employee(models.Model):

    first_name = models.CharField(max_length=20,null=True)
    last_name = models.CharField(max_length=20,null=True)
    email = models.EmailField(max_length=30,null=True)
    emp_id = models.CharField(max_length=10,null=True)
    mobile = models.CharField(max_length=10,null=True)


    def __str__(self):
        return str(self.first_name) + str(self.emp_id)

from django.contrib.auth.models import User

class New_Employee(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    username = models.CharField(max_length=20,null=True)
    first_name = models.CharField(max_length=20,null=True)
    last_name = models.CharField(max_length=20,null=True)
    email = models.EmailField(max_length=30,null=True)
    emp_id = models.CharField(max_length=10,null=True)
    mobile = models.CharField(max_length=10,null=True)
