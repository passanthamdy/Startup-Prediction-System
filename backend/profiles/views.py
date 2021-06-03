from django.shortcuts import render
from rest_framework import generics
from accounts.models import CustomUser
#from .serializer import UserProfileSerlialier



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
