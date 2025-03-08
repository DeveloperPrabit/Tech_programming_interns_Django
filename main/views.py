from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render
from .models import News, Category
from django.contrib.auth.decorators import login_required



# Create your views here.
def BASE(request):    
       return render(request,'base.html')

def BASE1(request):    
       return render(request,'base1.html')


def Index(request):
    postnews = News.objects.order_by('-posted_date')[:3]
    postnews1 = News.objects.all()[:4]
    category = Category.objects.all()[:4]
    recentnews = News.objects.order_by('-posted_date')[:5]

    context = {
        'postnews': postnews,
        'category': category,
        'recentnews': recentnews,
        'postnews1': postnews1
    }
    return render(request, 'index.html', context)  # Correct indentation

def About(request):
    first_page = Page.objects.first()
    context = {
        "first_page": first_page,  # Change key from "page" to "first_page"
    }
    return render(request, 'aboutus.html', context)

def Contact(request):
    first_page = Page.objects.first()
    context = {
        "first_page": first_page,  # Change key from "page" to "first_page"
    }
    return render(request, 'contactus.html', context)



def Category_details(request):
    first_page = Page.objects.first()
    context = {
        "page": first_page,
    }
    return render(request, 'includes1/header.html', context)

def category_detail(request, id):
    catid = get_object_or_404(Category, id=id)
    news_list = News.objects.filter(cat_id=catid).order_by('-posted_date')  # Order by published date, or any other field
    paginator = Paginator(news_list, 4)  # Show 5 news items per page

    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    
    return render(request, 'categorywise_newsdetail.html', {'catid': catid, 'news': news})



def View_singlenews(request, id):
    # Fetch the news article by ID
    sinnews = get_object_or_404(News, id=id)
    
    # Get the most recent 4 news articles
    recentnews = News.objects.order_by('-posted_date')[:4]
    
    # Get category counts
    category_counts = Category.objects.annotate(news_count=Count('news'))
    
    # Fetch the approved comments related to this news article
    comments_list = Comments.objects.filter(news_id=sinnews, status='Approved')
    
    # Handle the POST request to create a new comment
    if request.method == "POST":
        # Create and save the new comment
        comment_obj = Comments(
            news_id=sinnews,
            comment=request.POST['comment'],
            name=request.POST['name'],
            email=request.POST['email'],
        )
        comment_obj.save()
        return redirect('respect')  # Redirect to a thank you page or wherever you want

    # Prepare the context data to be passed to the template
    context = {
        "sinnews": sinnews,
        'recentnews': recentnews,
        'category_counts': category_counts,
        'comments_list': comments_list,
    }

    # Render the template with the context
    return render(request, 'single-news-details.html', context)



def Respect(request):
    return render(request, 'thankyou.html')


def Search(request): 
    query = request.GET.get('query', '').strip()  # Get query from GET request
    
    if query:
        searchnews = News.objects.filter(
            Q(posttitle__icontains=query) |
            Q(cat_id__catname__icontains=query) |
            Q(subcategory_id__subcatname__icontains=query)
        ).select_related('cat_id', 'subcategory_id')  # Optimized query

        if searchnews.exists():
            messages.info(request, f"Search results for: {query}")
        else:
            messages.info(request, f"No records found for: {query}")
        
        # Pagination
        paginator = Paginator(searchnews, 10)  # 10 results per page
        page = request.GET.get('page')

        try:
            searchnews_paginated = paginator.page(page)
        except PageNotAnInteger:
            searchnews_paginated = paginator.page(1)
        except EmptyPage:
            searchnews_paginated = paginator.page(paginator.num_pages)

        return render(request, 'search-news.html', {
            'searchnews': searchnews_paginated,
            'query': query,
        })
    
    else:
        messages.info(request, "Please enter a search query.")  # Message for empty query
        return render(request, 'search-news.html', {'searchnews': None})
        
def Category_detail(request, id):
    catid = get_object_or_404(Category, id=id)
    news_list = News.objects.filter(cat_id=catid).order_by('-posted_date')

    paginator = Paginator(news_list, 5)  # Show 5 news items per page
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)

    # Get category-wise news count for the sidebar
    category_counts = Category.objects.annotate(news_count=Count('news'))

    return render(request, 'categorywise_newsdetail.html', {
        'catid': catid,
        'news': news,
        'category_counts': category_counts
    })


def LOGIN(request):
    return render(request, 'login.html')  # Render login page if not authenticated






def doLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')  # 'on' if checked, otherwise None
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Set session expiry based on remember_me checkbox
            if remember_me:
                request.session.set_expiry(2592000)  # 30 days (in seconds)
            else:
                request.session.set_expiry(0)  # Session expires when browser is closed

            # Redirect user based on their type
            user_type = getattr(user, 'user_type', None)
            if user_type == '1':  # Intern
                return redirect(reverse('dashboard'))
            elif user_type == '2':  # Reader
                return redirect(reverse('dashboard'))
        else:
            # Show error message and keep the entered username and remember_me checkbox state
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html', {'username': username, 'remember_me': remember_me})

    else:
        # Handle non-POST requests (redirect to login page with an error message)
        messages.error(request, 'Invalid request method')
        return redirect(reverse('LOGIN'))#direct to login page

    return render(request,'login.html')