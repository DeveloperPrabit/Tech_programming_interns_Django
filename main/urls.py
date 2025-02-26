from django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name='index'),
    path('base/', BASE, name='base'),
    path('base1/', BASE1, name='base1'),
    path('about/', About, name='about'),
    path("contact/",Contact, name="contact"),
    path("respect/",Respect,name="respect"),
    path('view_single_news/<str:id>',View_singlenews, name='view_single_news'),
    path('category/<int:id>/',Category_detail, name='category_detail'),



]
