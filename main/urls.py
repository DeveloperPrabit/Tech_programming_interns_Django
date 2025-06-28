from django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name='index'),
    path('base/', BASE, name='base'),
    path('base1/', BASE1, name='base1'),
    path('about/', About, name='about'),
    path("contact/",contact_view, name="contact"),
    path("respect/",Respect,name="respect"),
    path('view_single_news/<str:id>',View_single_news, name='view_single_news'),
    path('category/<int:id>/',Category_detail, name='category_detail'),
    path('SearchNews/',Search, name='search_news'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/',UserRegisterView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='log_out'),
    #path('doLogin',doLogin, name='doLogin'),
    #path('Login',LOGIN, name='login'),




]
