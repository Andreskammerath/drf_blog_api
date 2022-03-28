from rest_framework import serializers
from post.models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        read_only = ('author',)
        model = Post