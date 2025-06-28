import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .mixins import TimestampMixin
from .managers import UserManager

class UserType(models.TextChoices):
    USER = 'user', _('User')
    ADMIN = 'admin', _('Admin')

<<<<<<< HEAD
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
=======

class CustomUser(AbstractBaseUser, PermissionsMixin, TimestampMixin):
    uuid = models.UUIDField(
        primary_key=True,
        editable=False,
        unique=True,
        default=uuid.uuid4
    )

    email = models.EmailField(
        _('email address'),
        unique=True, 
    )

    first_name = models.CharField(
        _('first name'),
        max_length=50,
        blank=True,
    )
    last_name = models.CharField(
        _('last name'),
        max_length=50,
        blank=True,
    )



    '''full_name = models.CharField(
        _('full name'),
        max_length=100,
        blank=True,
    )'''

    full_address = models.CharField(
        _('full address'),
        max_length=100,
        blank=True,
    )

    '''mobile = models.CharField(
        _('mobile'),
        max_length=15,
        blank=True,
    )'''

    profile_picture = models.ImageField(
        _('profile picture'),
        upload_to='profile_pictures/',
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    is_staff = models.BooleanField(
        default=False
    )

    user_type = models.CharField(
        _('user type'),
        max_length=5,
        choices=UserType.choices,
        default=UserType.USER
    )

    date_joined = models.DateTimeField(
        _('date joined'),
        auto_now_add=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        indexes = [
            models.Index(fields=['email'], name='email_idx'),
        ]
        ordering = ['-created_at']
>>>>>>> 1da1c77 (first commit)


# Category Model
class Category(models.Model):
    catname = models.CharField(max_length=200)
    catdes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
<<<<<<< HEAD
        return self.name
=======
        return self.catname
>>>>>>> 1da1c77 (first commit)


# Subcategory Model
class Subcategory(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcatname = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
<<<<<<< HEAD
        return f"{self.cat_id.name} - {self.subcatname}"

=======
        return self.subcatname
>>>>>>> 1da1c77 (first commit)

# News Model
class News(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_id = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
<<<<<<< HEAD
    posttitle = models.TextField(blank=True)
=======
    posttitle = models.CharField(max_length=255, blank=True)
>>>>>>> 1da1c77 (first commit)
    postdetails = models.TextField(blank=True)
    status = models.CharField(max_length=50)
    postimage = models.ImageField(upload_to='media/news/', null=True, blank=True)  # Image is optional
    postedby = models.CharField(max_length=50)
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updatedby = models.CharField(max_length=50)
    video_file = models.FileField(upload_to='media/videos/', blank=True, null=True)

    def __str__(self):
        return self.posttitle

    def __str__(self):
        return self.posttitle


# Page Model
class Page(models.Model):
    pagetitle = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    aboutus = models.TextField()
    email = models.EmailField(max_length=200)
    mobilenumber = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pagetitle


<<<<<<< HEAD
# Comments Model
=======
>>>>>>> 1da1c77 (first commit)
class Comments(models.Model):
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    status = models.CharField(max_length=250, blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
<<<<<<< HEAD
        return f"Comment by {self.name} on {self.news.posttitle}"
=======
        return f"Comment by {self.name}"
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
>>>>>>> 1da1c77 (first commit)
