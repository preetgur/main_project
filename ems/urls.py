from django.urls import path
from ems import views

urlpatterns = [

    path("",views.index,name="ems_index"),
    path("register_emp",views.register_employee,name="register_employee"),
    path("all_employees",views.all_employees,name="all_employees"),
    path("delete_employee/<str:pk>",views.delete_employee,name="delete_employee"),
    path("update_employee/<str:pk>",views.update_employee,name="update_employee"),
    path("employee_detail/<str:pk>",views.employee_detail,name="employee_detail"),
    path("employee_profile",views.employee_profile,name="employee_profile"),
    path("dashboard",views.dashboard,name="dashboard"),





]