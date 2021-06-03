from rest_framework import serializers
from .models import Profile
#from posts.serializers import PostSerializer


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        
        exclude = ['created_at']
