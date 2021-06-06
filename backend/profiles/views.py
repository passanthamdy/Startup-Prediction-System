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

# # @api_view(['GET'])
# # def UserProfile(request):
# #     userqs = request.user
# #     #postqs= Post.objects.filter(user_id=userqs.kwargs['user_id'])
# #     profile_serializer = ProfileSerializer(userqs)
# #     #post_serializer = PostSerializer(postqs, many= True)
# #     result_serializer= profile_serializer.data 
# #     return Response (result_serializer)


# class UserProfile(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = UserProfileSerlialier
#     def get_queryset(self):
#         return  CustomUser.select_related('profile').prefetch_related("posts").get(username=self.username)


class UpdateUserProfile(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.order_by('-created_at')
    serializer_class = ProfileSerializer
    lookup_field = 'id'

class UserPostsView(generics.ListAPIView):
    serializer_class= PostSerializer
    def get_queryset(self):
        qs = Post.objects.filter(user=self.kwargs['user'])
        return qs


