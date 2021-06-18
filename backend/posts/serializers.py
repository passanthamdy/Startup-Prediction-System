from rest_framework import serializers
from .models import Post,Dataset, Comment
from profiles.serializer import ProfileSerializer
from accounts.serializers import CustomUserSerializer


class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dataset 
        fields= '__all__'
        lookup_field= 'id'


class CreatePostSerializer(serializers.ModelSerializer):
    user= serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    class Meta:
        model=Post
        exclude = [ 'likes']

        
class CommentSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post']
        lookup_field = 'id'

class PostSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(source='user.profile', read_only=True)
    dataset= DatasetSerializer()
    total_likes = serializers.SerializerMethodField()
    likes= CustomUserSerializer(many=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model =  Post 
        exclude = ['featured']
        lookup_field= 'id'
        readonly_field = ['user','dataset', 'id','likes', 'total_likes']
    def get_total_likes(self,obj):
        return obj.likes.count()
   
