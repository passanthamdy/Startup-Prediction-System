from rest_framework import serializers
from .models import Post, Category, Comment
from accounts.serializers import CustomUserSerializer
from profiles.serializer import ProfileSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= ('name', 'id')
        

class PostSerializer(serializers.ModelSerializer):
    
    total_likes = serializers.SerializerMethodField()
    likes = CustomUserSerializer(many=True)
    class Meta:
        model = Post
        
        exclude = ['slug','featured']
        lookup_field = 'id'
        

    def get_total_likes(self, obj):
        return obj.likes.count()
    def to_representation(self, instance):
        rep =super().to_representation(instance)
        rep['profile'] = ProfileSerializer(instance.profile).data
        return rep 


class UserPost(serializers.ModelSerializer):
    class Meta:
        model = Post
        
        exclude = ['slug','featured']
        lookup_field = 'id'
