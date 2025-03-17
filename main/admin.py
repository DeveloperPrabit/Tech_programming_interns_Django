from django.contrib import admin
from .models import Category, Subcategory, News, Page, Comments, CustomUser
from django.contrib.auth.admin import UserAdmin

# Admin Panel customization
admin.site.site_header = 'News Admin Panel'
admin.site.index_title = 'News Portal'
admin.site.site_title = 'Welcome to Online News Portal'

# CustomUser Admin
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_type', 'is_staff', 'is_active', 'profile_pic')
    list_filter = ('user_type', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ['username']
    
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('user_type', 'profile_pic')}), 
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}), 
        ('Important dates', {'fields': ('last_login', 'date_joined')}), 
    )
    
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password', 'user_type', 'profile_pic', 'is_active', 'is_staff', 'groups', 'user_permissions')
        }),
    )

# Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')  # Changed 'catname' to 'name'
    search_fields = ('name',)  # Changed 'catname' to 'name'

# Subcategory Admin
@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('subcatname', 'cat_id', 'created_at')  # Ensure 'subcatname' exists in models.py
    search_fields = ('subcatname',)
    list_filter = ('cat_id',)

# News Admin
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'posttitle', 'cat_id', 'postedby', 'posted_date')  # Ensured fields are correct
    list_filter = ('cat_id', 'posted_date')

# Page Admin
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('pagetitle', 'email', 'mobilenumber', 'created_at')  # Ensure fields match models.py
    search_fields = ('pagetitle', 'email')

# Comments Admin
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('news_id', 'name', 'email', 'status', 'posted_date')  # Ensured fields match models.py
    search_fields = ('name', 'email')
    list_filter = ('status', 'posted_date')
