from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User as CustomUser  # Assuming you have a custom User model

# Form for user registration
class CustomUserForm(UserCreationForm):
    # Username field with custom styling
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter User Name'})
    )
    # Email field with custom styling
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'})
    )
    # Password1 field with custom styling
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Password'})
    )
    # Password2 field with custom styling
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Your Password'})
    )

    class Meta:
        model = CustomUser  # If you're using a custom user model, otherwise use 'User'
        fields = ['username', 'email', 'password1', 'password2']

# Form for user login
class LoginForm(forms.Form):
    # Username field
    username = forms.CharField(
        max_length=100,
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'})
    )
    # Password field
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
        label='Password'
    )

