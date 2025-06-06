from rest_framework import permissions

class IsParticipantOrReadOnly(permissions.BasePermission):
    """Allow access only to participants of a conversation"""

    def has_object_permission(self, request, view, obj):
        return request.user in obj.participants.all()


class IsParticipantOfConversation(permissions.BasePermission):
    """Allow only participants in a conversation to access messages"""
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'participants'):
            return request.user in obj.participants.all()
        elif hasattr(obj, 'conversation'):
            return request.user in obj.conversation.participants.all()
        return False
