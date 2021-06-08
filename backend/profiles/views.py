from django.shortcuts import render
from rest_framework import generics
from .models import Profile
from posts.serializers import PostSerializer
from posts.models import Post
from .serializer import ProfileSerializer
from rest_framework import views
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import api_view
from .permissions import UserWritePermission
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions


class UpdateUserProfile(generics.RetrieveUpdateAPIView,UserWritePermission):
    permission_classes =[UserWritePermission]
    queryset = Profile.objects.order_by('-created_at')
    serializer_class = ProfileSerializer
    lookup_field = 'id'
 



class UserPostsView(generics.ListAPIView):
    serializer_class= PostSerializer
    def get_queryset(self):
        qs = Post.objects.filter(user=self.kwargs['user'])
        return qs


