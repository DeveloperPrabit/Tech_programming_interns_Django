from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterPage, name="RegisterPage"),
    path('login/', views.LoginPage, name="LoginPage"),
    path('logout/', views.logout_view, name='logout'),

]
