from rest_framework import serializers
from .models import Post
from profiles.serializer import ProfileSerializer
from accounts.serializers import CustomUserSerializer


class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
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
    total_likes = serializers.SerializerMethodField()
    likes= CustomUserSerializer(many=True)
    class Meta:
        model =  Post
        exclude = ['slug', 'featured']
        lookup_field= 'id'
    def get_total_likes(self,obj):
        return obj.likes.count()
   

    
