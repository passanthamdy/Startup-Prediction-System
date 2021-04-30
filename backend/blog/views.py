from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import  BlogPost ,Categories
from .serializers import BlogPostSerializer ,CategoriesSerializer


class BlogPostListView(ListAPIView):
    queryset=BlogPost.objects.order_by('date_created')
    serializer_class=BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class CategoriesListView(ListAPIView):
    queryset=Categories.objects.all()
    serializer_class=CategoriesSerializer
    lookup_field = 'name'
    permission_classes = (permissions.AllowAny, )

class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )


