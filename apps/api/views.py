from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .serializers import *

from apps.account.models import CustomUser
from apps.post.models import Post

class CustomUserViewSet(ModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]

class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [IsAdminUser]
