from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register('user', CustomUserViewSet, basename='user')
router.register('post', PostViewSet, basename='post')


urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),

]

urlpatterns += router.urls