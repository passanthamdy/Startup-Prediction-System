from rest_framework import serializers
from .models import  Message





class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField("get_sender_data")
    sender_id = serializers.IntegerField(write_only=True)
    receiver = serializers.SerializerMethodField("get_receiver_data")
    receiver_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Message
        fields = "__all__"

    def get_receiver_data(self, obj):
        from accounts.serializers import UserProfileSerializer
        return UserProfileSerializer(obj.receiver.user_profile).data

    def get_sender_data(self, obj):
        from accounts.serializers import UserProfileSerializer
        return UserProfileSerializer(obj.sender.user_profile).data