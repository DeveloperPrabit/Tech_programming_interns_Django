from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, Post

def context_data():
    return {
        'site_name': 'Simple News Portal',
        'page': 'home',
        'page_title': 'News Portal',
        'categories': Category.objects.filter(status=1).all(),
    }

def home(request):
    context = context_data()
    posts = Post.objects.filter(status=1).order_by('-date_created').all()
    
    context['page'] = 'home'
    context['page_title'] = 'Home'
    context['latest_top'] = posts[:2]
    context['latest_bottom'] = posts[2:12]
    
    return render(request, 'main/home.html', context)

def category_post(request, pk=None):
    context = context_data()
    if pk is None:
        messages.error(request, "File not Found")
        return redirect('home')

    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist:
        messages.error(request, "File not Found")
        return redirect('home')

    context['category'] = category
    context['page'] = 'category_post'
    context['page_title'] = f'{category.name} Posts'
    context['posts'] = Post.objects.filter(status=1, category=category).all()
    context['latest'] = Post.objects.filter(status=1).order_by('-date_created').all()[:10]
    
    return render(request, 'main/category.html', context)
