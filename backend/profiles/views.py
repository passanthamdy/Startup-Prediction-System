# from django.shortcuts import render
# from rest_framework import generics
# from rest_framework.authtoken.views import APIView
# from rest_framework.response import Response
# from rest_framework.status import HTTP_200_OK
# from .models import Profile
# from .serializer import ProfileSerializer,ProfileSerializer
# from accounts.models import CustomUser
# from accounts.serializers import CustomUserSerializer
# from posts.models import Postgi
# from posts.serializers import PostSerializer
# from rest_framework.decorators import api_view

# # @api_view(['GET'])
# # def UserProfile(request):
# #     userqs = request.user
# #     #postqs= Post.objects.filter(user_id=userqs.kwargs['user_id'])
# #     profile_serializer = ProfileSerializer(userqs)
# #     #post_serializer = PostSerializer(postqs, many= True)
# #     result_serializer= profile_serializer.data 
# #     return Response (result_serializer)


# class UserProfile(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ProfileSerializer
#     def get_queryset(self):
#         return  CustomUser.select_related('profile').prefetch_related("posts").get(username=self.username)
