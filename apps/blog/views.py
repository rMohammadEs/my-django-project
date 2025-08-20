from rest_framework import viewsets
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostDetailSerializer