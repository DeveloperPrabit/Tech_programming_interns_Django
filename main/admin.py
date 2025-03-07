from django.contrib import admin
from .models import Category, Subcategory, News, Page, Comments,CustomUser
from django.contrib.auth.admin import UserAdmin



admin.site.site_header = 'News Admin Panel'        
admin.site.index_title = 'News_portal'                
admin.site.site_title = 'Welcome to  Online News portal' 

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
        (None, {'fields': ('username', 'email', 'password', 'user_type', 'profile_pic', 'is_active', 'is_staff', 'groups', 'user_permissions')}),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('catname', 'created_at', 'updated_at')
    search_fields = ('catname',)

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('subcatname', 'cat_id', 'created_at')
    search_fields = ('subcatname',)
    list_filter = ('cat_id',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'posttitle', 'cat_id', 'postedby', 'posted_date')
    list_filter = ('cat_id', 'posted_date')

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('pagetitle', 'email', 'mobilenumber', 'created_at')
    search_fields = ('pagetitle', 'email')

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('news_id', 'name', 'email', 'status', 'posted_date')
    search_fields = ('name', 'email')
    list_filter = ('status', 'posted_date')
