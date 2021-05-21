
from rest_framework import serializers
from .models import Post, Category, Comment
from rest_framework.fields import CurrentUserDefault


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= ('name', 'id')
        

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'
        lookup_field = 'slug'
        

