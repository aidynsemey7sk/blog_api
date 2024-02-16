from rest_framework import generics, viewsets
from blog.models import Post
from .serializers import PostSerializer


class ListPost(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
