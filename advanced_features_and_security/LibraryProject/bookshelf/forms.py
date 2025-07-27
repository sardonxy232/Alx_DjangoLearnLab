# bookshelf/forms.py

from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']

class UserRegistrationForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'date_of_birth', 'profile_photo', 'password1', 'password2']
