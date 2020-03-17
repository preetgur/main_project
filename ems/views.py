from django.shortcuts import render,redirect
from ems.forms import Register_Emp_Form
# Create your views here.


def index(request):

    context={}
    return render(request,"ems/index.html",context)


def register_employee(request):
    form = Register_Emp_Form()

    if request.method == "POST" :
        form = Register_Emp_Form(request.POST)
        if form.is_valid():
            form.save()
            print("Successfully Register Employee")
        
            return redirect('ems_index')

    context={"form":form}
    return render(request,"ems/register_employee.html",context)

from ems.models import Register_Employee
from ems.filters import Employee_filter

def all_employees(request):

    employees = Register_Employee.objects.all()
    total_emp = employees.filter().count()

    my_filter= Employee_filter(request.POST,queryset=employees)
    employees = my_filter.qs  # make query on employees
    context = {
        "all_employees":employees,
        "total_emp":total_emp,
        "my_filter":my_filter
        }
    return render(request,"ems/all_employee.html",context)


def delete_employee(request,pk):

    emp = Register_Employee.objects.get(id = pk)
    emp.delete()

    return redirect("all_employees")


def update_employee(request,pk):

    employee = Register_Employee.objects.get(id = pk)
    # from = Register_Emp_Form()   # create empty form
    form = Register_Emp_Form(instance=employee)  # create filled form
    
    if request.method == "POST":
        # form = Register_Emp_Form(request.POST)  # it create new entry in database
        form = Register_Emp_Form(request.POST,instance=employee)
        if form.is_valid():
            username = form.cleaned_data.get("first_name")
            print(username)
            form.save()
            return redirect("all_employees")
    


    context = {"form":form}
    return render(request,'ems/register_employee.html',context)


def employee_detail(request,pk):

    employee = Register_Employee.objects.get(id = pk)

    context = {"employee_detail":employee}
    return render(request,"ems/employee_detail.html",context)

from ems.forms import User_Form
from django.contrib import messages
from django.contrib.auth.models import Group
from ems.models import New_Employee
from django.contrib.auth import authenticate,login,logout
def employee_profile(request):

    form = User_Form()

    if request.method == "POST":
        form = User_Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            print("$$$ username ",username,password)
            messages.success(request,"Accounts created Successfuly!")
            profile = form.save() # contains the fields of User_Form

            group = Group.objects.get(name='employee')
            profile.groups.add(group)

            New_Employee.objects.create( 
                                    user= profile,
                                    username = profile.username,
                                    email = profile.email,  
                                    )  
            print("Added to employee group")  

            user = authenticate(request,username=username,password=password)
        
            if user is not None : 
                login(request,user)
                return redirect('dashboard')
            else:
                messages.info(request,"Invalid username or password !!!")
                                  

    context = {"form":form}
    return render(request,"ems/employee_profile.html",context)




def dashboard(request):

    context = {}

    return render(request,'ems/dashboard.html',context)