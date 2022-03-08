from rest_framework import serializers
from post.models import Post
from user_app.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer

    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        read_only = ('author',)
        model = Post