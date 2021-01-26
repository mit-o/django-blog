from ..models import Post
from .serializers import PostSerializer
from rest_framework import viewsets, permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        query = dict(self.request.query_params)
        count = self.request.query_params.get('count')
        user = self.request.query_params.get('user')
        fltr = dict()
        if user:
          fltr["author__username"] = user
        posts = Post.objects.filter(**fltr)
        if count:
          posts = posts[:int(count)]
        return posts
        
