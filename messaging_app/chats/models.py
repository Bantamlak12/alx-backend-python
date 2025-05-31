""" models.py: Defines custom user, conversations, and messaging models.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """A user model which is an extension of the Abstract user."""
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)


class Coversation(models.Model):
    """A model that tracks which users are involved in a conversation."""
    participants = models.ManyToManyField('CustomUser', related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    """ A model that define messaging between users."""
    conversation = models.ForeignKey(Coversation, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey('CustomUser', related_name='sent_message', on_delete=models.CASCADE)
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
