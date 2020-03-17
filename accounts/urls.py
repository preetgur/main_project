from django.urls import path
from  accounts  import views

# for reset the password
from django.contrib.auth import views as auth_views  

# python list
urlpatterns = [ 

    path("login",views.login_page,name="login"),
    path("register",views.register,name="register"),
    path("logout",views.logout_page,name="logout"),


    # using bulit in class based views to reset password and their name is also predefined
    # password_reset: Form where the user submit the email address
    path("reset_password/",auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),name="reset_password"),
    
    # password_reset_done: Page displayed to the user after submitting the email form. Usually with instructions to open the email account, look in the spam folder etc. And asking for the user to click on the link he will receive.
      path("reset_password_sent/",auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"),name="password_reset_done"),

    # password_reset_confirm: The link that was emailed to the user. This view will validate the token and display a password form if the token is valid or an error message if the token is invalid
    path("reset/<uidb64>/<token>/",
    auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"),
    name="password_reset_confirm"),

    # password_reset_complete: Page displayed to the user after the password was successfully changed.
    path("reset_password_complete/",
    auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"),
    name="password_reset_complete"),

]