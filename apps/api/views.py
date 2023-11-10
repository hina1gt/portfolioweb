from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAdminUser
from .serializers import *
import requests
from rest_framework.response import Response
from rest_framework.status import *
from drf_spectacular.utils import extend_schema

from apps.account.models import CustomUser
from apps.post.models import Post
from src.settings.base import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

class CustomUserViewSet(ViewSet):

    @extend_schema(responses=CustomUserSerializer)
    def list(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data, status=200)
    
    @extend_schema(responses=CustomUserSerializer)
    def create(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            chat_id = TELEGRAM_CHAT_ID
            message = f'Title: {serializer.instance.title}\nDescription: {serializer.instance.description}'
            bot_token = TELEGRAM_BOT_TOKEN
            url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
            payload = {
                'chat_id': chat_id,
                'text': message
            }
            response = requests.post(url, data=payload)
            
            if response.status_code == 200:
                return Response(serializer.data, status=201)
            else:
                return Response({'error': 'Failed to send message'}, status=500)
        return Response(serializer.errors, status=400)
            
    @extend_schema(responses=CustomUserSerializer)
    def retrieve(self, request, pk=None):
        user = CustomUser.objects.get(pk=pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=200)
    
    @extend_schema(request=CustomUserSerializer, responses=CustomUserSerializer)
    def partial_update(self, request, pk=None):
        user = CustomUser.objects.get(pk=pk)
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def destroy(self, request, pk=None):
        user = CustomUser.objects.get(pk=pk)
        user.delete()
        return Response(status=204)

class PostViewSet(ViewSet):

    @extend_schema(responses=PostsSerializer(many=True))
    def list(self, request):
        posts = Post.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data, status=200)
    
    @extend_schema(responses=PostsSerializer())
    def create(self, request):
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    @extend_schema(responses=PostsSerializer())
    def retrieve(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        serializer = PostsSerializer(post)
        return Response(serializer.data, status=200)
    
    @extend_schema(request=PostsSerializer(), responses=PostsSerializer())
    def partial_update(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        serializer = PostsSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def destroy(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        post.delete()
