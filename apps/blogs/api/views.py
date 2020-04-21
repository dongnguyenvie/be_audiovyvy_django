from rest_framework import generics, permissions
from blogs.models import Blog
from blogs.api.serializers import BlogSerializer
# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

class BlogListAPIView(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
class BlogAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    # permission_classes = []
    # lookup_url_kwarg = 'id'
    # lookup_field = 'id'