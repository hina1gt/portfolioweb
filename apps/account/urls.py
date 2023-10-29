from django.urls import path, include
from . import views
from django.contrib.auth.views import *


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]