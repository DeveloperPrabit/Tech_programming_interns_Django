from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterPage, name="RegisterPage"),
    path('login/', views.LoginPage, name="LoginPage"),
    path('logout/', views.Log_out, name="log_out"),

]
