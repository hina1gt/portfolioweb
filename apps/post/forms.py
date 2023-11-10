from django import forms
from .models import *
from apps.account.models import CustomUser

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = 'title', 'image', 'description'

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'icon', 'about' ]