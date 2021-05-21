from django.shortcuts import render
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import AllowAny

#from django_filters.rest_framework import DjangoFilterBackend
#next update >> APIVIEW instead of generics
#dont forget to remove allowany permission
class CategoryCreateView(generics.ListCreateAPIView):
    queryset  = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


#after applying machine learning it would be only list View, 
#dont forget to remove allowany permission
class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['featured']
    permission_classes = [AllowAny]

    
#dont forget to remove allowany permission
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]
