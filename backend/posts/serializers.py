from rest_framework import serializers
from .models import Post,Dataset
from profiles.serializer import ProfileSerializer
from accounts.serializers import CustomUserSerializer


class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dataset 
        fields= '__all__'


class CreatePostSerializer(serializers.ModelSerializer):
    user= serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    class Meta:
        model=Post
        exclude = ['slug', 'likes']

class PostSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(source='user.profile', read_only=True)
    dataset= DatasetSerializer()
    total_likes = serializers.SerializerMethodField()
    likes= CustomUserSerializer(many=True)
    class Meta:
        model =  Post 
        exclude = ['slug', 'featured']
        lookup_field= 'id'
        readonly_field = ['user','dataset', 'id','likes', 'total_likes']
    def get_total_likes(self,obj):
        return obj.likes.count()
   
