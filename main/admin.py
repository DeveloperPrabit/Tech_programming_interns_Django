from django.contrib import admin
from .models import Category, Subcategory, News, Page, Comments

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
