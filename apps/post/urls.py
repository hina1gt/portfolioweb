from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('post/', post, name='post'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    path('post/<int:pk>/update/', post_update, name='post_update'),
    path('create/', post_create, name='post_create'),
    path('edit/', edit, name='edit',)
]