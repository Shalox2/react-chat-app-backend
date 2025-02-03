from unittest.util import _MAX_LENGTH
from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.CharField(max_length=255, blank=False)
    password = models.CharField(max_length=255, blank=False)
    def __str__(self):
        return str(self.name)

class Chat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=False, related_name="room")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, related_name="chatUser")
    message = models.TextField(blank=True)
    image = ResizedImageField(force_format='WEBP', size=None,scale=0.5, quality=75, upload_to='images', blank=True, null=True)

    # def __str__(self):
    #     return str(self.room)
    from django.db import models

class Message(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    reply_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.user}: {self.content}"
