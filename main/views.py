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
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import ContactForm,UserLoginForm
from django.contrib.auth import get_user_model
from django.utils import timezone





# Create your views here.
def BASE(request):    
    return render(request,'base.html')

def BASE1(request):    
       return render(request,'base1.html')

def Index(request): 
    postnews = News.objects.order_by('-posted_date')[:3]
    postnews1 = News.objects.all()[:4]
    category = Category.objects.all()  # ✅ Show ALL categories
    recentnews = News.objects.order_by('-posted_date')[:5]
    first_page = Page.objects.first()

    context = {
        'postnews': postnews,
        'category': category,  # now full list
        'recentnews': recentnews,
        'postnews1': postnews1,
        'first_page': first_page
    }
    return render(request, 'index.html', context)

def About(request):
    first_page = Page.objects.first()
    context = {
        "first_page": first_page,  # Change key from "page" to "first_page"
    }
    return render(request, 'aboutus.html', context)






def Category_details(request):
    first_page = Page.objects.first()
    categories = Category.objects.all()  # fetch all categories here

    context = {
        "page": first_page,
        "category": categories,          # pass categories for navbar
    }
    return render(request, 'includes1/header.html', context)


def category_detail(request, id):
    catid = get_object_or_404(Category, id=id)
    news_list = News.objects.filter(cat_id=catid).order_by('-posted_date')
    paginator = Paginator(news_list, 4)  # 4 news per page

    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)

    categories = Category.objects.all()  # fetch categories for navbar here too

    context = {
        'catid': catid,
        'news': news,
        'category': categories,          # pass categories for navbar
    }
    return render(request, 'categorywise_newsdetail.html', context)


def View_single_news(request, id):
    # Fetch the news article by ID
    sinnews = get_object_or_404(News, id=id)
    categories = Category.objects.all()
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
        'category': categories ,
    }

    # Render the template with the context
    return render(request, 'single-news-details.html', context)


def Respect(request):
    categories = Category.objects.all()
    return render(request, 'thankyou.html', {
        'category': categories
    })



def Search(request): 
    query = request.GET.get('query', '').strip()
    
    categories = Category.objects.all()

    if query:
        searchnews = News.objects.filter(
            Q(posttitle__icontains=query) |
            Q(cat_id__catname__icontains=query) |
            Q(subcategory_id__subcatname__icontains=query)
        ).select_related('cat_id', 'subcategory_id')

        if searchnews.exists():
            messages.info(request, f"Search results for: {query}")
        else:
            messages.info(request, f"No records found for: {query}")

        paginator = Paginator(searchnews, 10)
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
            'category': categories,
        })
    else:
        messages.info(request, "Please enter a search query.")
        return render(request, 'search-news.html', {
            'searchnews': None,
            'query': '',
            'category': categories
        })

        


def Category_details(request):
    first_page = Page.objects.first()
    categories = Category.objects.all()  # fetch all categories here

    context = {
        "page": first_page,
        "category": categories,          # pass categories for navbar
    }
    return render(request, 'includes1/header.html', context)


def Category_detail(request, id):
    catid = get_object_or_404(Category, id=id)
    news_list = News.objects.filter(cat_id=catid).order_by('-posted_date')
    paginator = Paginator(news_list, 4)  # 4 news per page

    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)

    categories = Category.objects.all()  # fetch categories for navbar here too

    context = {
        'catid': catid,
        'news': news,
        'category': categories,          # pass categories for navbar
    }
    return render(request, 'categorywise_newsdetail.html', context)


def contact_view(request):
    first_page = Page.objects.first()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Manually save Contact instance
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message'],
            )
            messages.success(request, "Message sent successfully!")
            return redirect('contact')  # Make sure this matches your URL name
    else:
        form = ContactForm()

    context = {
        'form': form,
        'first_page': first_page,
    }
    return render(request, 'contactus.html', context)


CustomUser = get_user_model()

class UserRegisterView(View):
    template_name = 'register.html'
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse("dashboard"))
        categories = Category.objects.all()
        return render(request, self.template_name, {"category": categories})

    
    def post(self, request):
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        password = request.POST.get('password')
        full_address = request.POST.get('full_address')
        terms = request.POST.get('terms')

        errors = []

        # Validate required fields
        if not all([full_name, full_address, email, password, terms]):
            errors.append("All fields are required.")


        # Validate unique email
        if CustomUser.objects.filter(email=email).exists():
            errors.append("This email is already registered.")

        # Validate password length
        if len(password) < 8:
            errors.append("Password must be at least 8 characters long.")

        if not terms:
            messages.error(request, "You must accept the terms and conditions.")

        if errors:
            for error in errors:
                messages.error(request, error)
            # Send back the filled data
            return render(request, self.template_name, {
                "email": email,
                "full_name": full_name,
                "full_address": full_address,

            })
        
        # Create user
        user = CustomUser.objects.create(
            email=email,
            full_name=full_name,
            full_address=full_address,
        )
        user.set_password(password)
        user.save()

        messages.success(request, "Registration successful. You can now log in.")
        return redirect("login")


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect("index")

    def post(self, request):
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect("index")
    



class UserLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("dashboard")
        form = UserLoginForm()
        categories = Category.objects.all()
        return render(request, 'login.html', {'form': form, 'category': categories})


    def post(self, request):
        category = Category.objects.all()
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)

                # Redirect based on user type
                user_type = getattr(user, 'user_type', None)
                if user_type == UserType.ADMIN:
                    return redirect(reverse('dashboard'))
                elif user_type == UserType.USER:
                    return redirect(reverse('index'))
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid form submission')

        return render(request, 'login.html', {'form': form})
