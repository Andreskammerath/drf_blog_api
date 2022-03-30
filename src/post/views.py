from django.contrib.auth import get_user_model
from rest_framework import viewsets
from post.models import Post
from post.serializers import PostSerializer, UserSerializer
from post.permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer