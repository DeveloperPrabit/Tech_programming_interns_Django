from django.contrib.auth.forms import (
    UserCreationForm, 
    UserChangeForm, 
    AuthenticationForm,
    
)
from django import forms
from.models import CustomUser,Contact
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserChangeForm(UserChangeForm):
    
        class Meta:
            model = CustomUser
            fields = '__all__'

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True, 'class':'form-control', 'placeholder': 'Email'}), label="Email")
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})






class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
       
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',

    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
       
        'rows': 5,
    }))
