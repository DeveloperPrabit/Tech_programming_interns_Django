from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('category/<int:pk>/', views.category_post, name="category-post"),  # Corrected function reference
]
