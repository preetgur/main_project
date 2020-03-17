from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.

from accounts.forms import Register_Form
def register(request):

    form = Register_Form()

    if request.method =="POST":
        form = Register_Form(request.POST)
     
        if form.is_valid():
            username = form.cleaned_data.get('username')
            
            form.save()
            messages.success(request,f"Register Successfully..! {username}")

            return redirect("login")   # Realted to url name

    context = {"form":form}
    return render(request,'accounts/register.html',context)


# Using Django built in login-authenticate function

from django.contrib.auth import authenticate, login

def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        
        if user is not None : 
            login(request,user)
            return redirect('')
        else:
            messages.info(request,"Invalid username or password !!!")

    return render(request,"accounts/login.html")



##################### Logout ######################
from django.contrib.auth import logout


def logout_page(request):
    
    logout(request)
    return redirect("login")
