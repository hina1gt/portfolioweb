from django.db.models import *
from django.urls import reverse
from apps.account.models import *

class Post(Model):

    title = CharField(max_length=20)
    description = TextField(blank=True, null=True)
    image = ImageField(upload_to='posts-images')
    created = DateField(auto_now_add=True)
    updated = DateField(auto_now=True)
    author = ForeignKey(CustomUser, on_delete=CASCADE)

    def get_absolute_url(self):
        return reverse(
            'post_detail', 
            args=[self.pk]
        )
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.title}'
    
    


