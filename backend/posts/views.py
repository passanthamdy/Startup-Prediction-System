from django.shortcuts import get_object_or_404, render
from .models import Post, Category
from .serializers import PostSerializer 
from profiles.serializer import ProfileSerializer
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import APIView
from rest_framework.response import Response

#from django_filters.rest_framework import DjangoFilterBackend
#next update >> APIVIEW instead of generics
#dont forget to remove allowany permission
# class CategoryCreateView(generics.ListCreateAPIView):
#     queryset  = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [AllowAny]


#after applying machine learning it would be only list View, 
#dont forget to remove allowany permission
#DONE
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']
    #permission_classes = [AllowAny]

    
#dont forget to remove allowany permission
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer
    lookup_field = 'id'
    #permission_classes = [AllowAny]


class PostLike(APIView):

    def get(self, request, slug = None, format=None):
        obj = get_object_or_404(Post, slug=slug)
        url_ = obj.get_abslute_url()
        user = self.request.user
        updated = False
        liked = False
        if user.is_authnticated():
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else :
                liked= True
                obj.likes.add(user)
            updated= True
            data ={
                "updated": updated,
                "liked": liked
            }

        

        return Response(data)