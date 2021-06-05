from rest_framework import serializers
from .models import Post, Category, Comment,Dataset
from profiles.serializer import ProfileSerializer
from accounts.serializers import CustomUserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= ('name', 'id')


class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model= Dataset
        fields='__all__' 

class PostSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(source='user.profile', read_only=True)
    total_likes = serializers.SerializerMethodField()
    likes= CustomUserSerializer(many=True)
    class Meta:
        model =  Post
        exclude = ['slug', 'featured']
        lookup_field= 'id'
    def get_total_likes(self,obj):
        return obj.likes.count()
    



#     def get_total_likes(self, obj):
#         return obj.likes.count()
#     def to_representation(self, instance):
#         rep =super().to_representation(instance)
#         rep['profile'] = ProfileSerializer(instance.profile).data
#         return rep 
