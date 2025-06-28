from django.urls import path
from .views import *
from .adminprofile import *

urlpatterns = [
  path("dashboard/",dashboard,name="dashboard"),
  path("manage_subcategory/",Manage_subcategory,name="manage_subcategory"),
  path("manage_post/",Manage_posts,name="manage_posts"),
  path("manage_subadmin/",Manage_subadmin,name="manage_subadmin"),
  path("manage_category/",Manage_category,name="manage_category"),
  path("add_subadmin/",Add_subadmin,name="add_subadmin"),
  path("add_category/",Add_category,name="add_category"),
  path("add_subcategory/",Add_subcategory,name="add_subcategory"),
  path("add_post/",Add_post,name="add_post"),
  path("all_comments/",All_comments,name="all_comments"),
  path("approved_comments/",Approved_comments,name="approved_comments"),
  path("unapproved_comments/",Unapproved_comments,name="unapproved_comments"),
  path("website_update/",Website_update,name="website_update"),
  path("update_category_details/<int:id>/",Update_category,name="update_category"),
  path("delete_category/<int:id>/", Delete_category, name="delete_category"),
  path('UpdateCategoryDetails', Update_category_details, name='update_category_details'),
  path('update_subcategory<int:id>',Update_subcategory, name='update_subcategory'),
  path("update_subcategory_details/",Update_subcategory_details,name="update_subcategory_details"),
  path("delete_subcategory<int:id>/",Delete_subcategory,name="delete_subcategory"),
  path('ViewsPosts/<int:id>/',Views_post, name='views_posts'),
  path('DeletePosts/<str:id>',Delete_post, name='delete_posts'),
  path('UpdatePost/',Update_post, name='update_post'),
  path('DeleteSubadmin/<str:id>',Delete_subadmin, name='delete_subadmin'),
  path('ManageSubadmin/',Manage_subadmin, name='manage_subadmin'),
  path('ViewSubadmin/<str:id>',View_subadmin, name='view_subadmin'),
  path('SubadminProfile/update/',Subadmin_profile_update, name='subadmin_profile_update'),
  path('comment/<int:id>/',View_comment,name="view_comment"),
  path('DeleteComments/<str:id>/',Delete_comments, name='delete_comments'),
  path('UpdateCommentsStatus/', Update_comment_status, name='update-comments-status'),
  path('Password/', CHANGE_PASSWORD, name='change_password'),

  #for admin profile\
    path('adminprofile/',admin_profile, name='admin_profile'),
    path("adminprofile_update/,",admin_profile_update,name="admin_profile_update")
]