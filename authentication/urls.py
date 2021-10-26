from django.urls import path 
from . import views

app_name = 'authentication'

urlpatterns = [
    path('signup/', views.SignUp, name="signup"),
    path('signup/normal_signup/', views.NormalSignUp, name="NormalSignUp"),
    path('signup/ngo_signup/', views.NGOSignUp, name="NGOSignUp"), 
    path('signup/doctor_signup/', views.DoctorSignUp, name="DoctorSignUp"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),   
]
