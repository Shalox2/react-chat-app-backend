from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Chat,Message

from rest_framework import serializers

class ChatSerializer(ModelSerializer):
    user = SerializerMethodField("get_name")
    class Meta:
        model = Chat
        fields = '__all__'
    def get_name(self, obj):
        return obj.user.username
    
    
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content', 'user', 'timestamp', 'reply_to']

    def create(self, validated_data):
        # Handle the creation of a message, including the reply_to field
        return Message.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Handle the update of a message if needed
        instance.content = validated_data.get('content', instance.content)
        instance.reply_to = validated_data.get('reply_to', instance.reply_to)
        instance.save()
        return instance