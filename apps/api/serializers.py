from rest_framework.serializers import ModelSerializer
from apps.account.models import CustomUser
from apps.post.models import Post

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'about', 'icon', 'first_name', 'last_name']

        def get_image(self, obj):
            request = self.context.get('request')
            if obj.image:
                image = obj.image.url
                return request.build_absolute_uri(image)
            return None

class PostsSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

        def get_image(self, obj):
            request = self.context.get('request')
            if obj.image:
                image = obj.image.url
                return request.build_absolute_uri(image)
            return None