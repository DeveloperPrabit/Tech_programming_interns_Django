from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# CustomUser Model
class CustomUser(AbstractUser):
    USER_TYPES = [
        ('1', 'admin'),
        ('2', 'subadmin')
    ]
    user_type = models.CharField(choices=USER_TYPES, max_length=50, default='1')  
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

    def __str__(self):
        return self.username


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Subcategory Model
class Subcategory(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcatname = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cat_id.name} - {self.subcatname}"


# News Model
class News(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_id = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    posttitle = models.TextField(blank=True)
    postdetails = models.TextField(blank=True)
    status = models.CharField(max_length=50)
    postimage = models.ImageField(upload_to='media/news')
    postedby = models.CharField(max_length=50)
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updatedby = models.CharField(max_length=50)

    def __str__(self):
        return self.posttitle


# Page Model
class Page(models.Model):
    pagetitle = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    aboutus = models.TextField()
    email = models.EmailField(max_length=200)
    mobilenumber = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pagetitle


# Comments Model
class Comments(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    status = models.CharField(max_length=250, blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.news.posttitle}"
