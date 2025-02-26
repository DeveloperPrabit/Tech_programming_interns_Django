from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages




# Create your views here.
def BASE(request):    
       return render(request,'base.html')

def BASE1(request):    
       return render(request,'base1.html')
from django.shortcuts import render
from .models import News, Category

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
    return render(request, 'aboutus.html')

def Contact(request):
    return render(request, 'contactus.html')

def category_detail(request):
    first_page = Page.objects.first()
    context = {
        "page": first_page,
    }
    return render(request, 'contactus.html', context)


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
        return redirect('thank_you')  # Redirect to a thank you page or wherever you want

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


def SEARCH_NEWS(request):
    if request.method == "GET":
        query = request.GET.get('query', '')
        if query:
            # Filter records where posttitle, category name, or subcategory name contains the query
            searchnews = News.objects.filter(
                Q(posttitle__icontains=query) |
                Q(cat_id__catname__icontains=query) |
                Q(subcategory_id__subcatname__icontains=query)
            ).select_related('cat_id', 'subcategory_id')  # Optimizing query

            if searchnews.exists():
                messages.info(request, "Search results for: " + query)
            else:
                messages.info(request, "No records found for: " + query)
            
            # Set up pagination
            paginator = Paginator(searchnews, 10)  # Show 10 search results per page
            page = request.GET.get('page', 1)
            
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
            messages.info(request, "Please enter a search query.")  # Adding message for empty query
            return render(request, 'search-news.html', {})
        
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
