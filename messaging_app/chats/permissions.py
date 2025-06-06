from rest_framework import permissions


class IsParticipantOrReadOnly(permissions.BasePermission):
    """Allow read-only access for everyone, but restric to participants of a conversation"""
    def has_object_permission(self, request, view, obj):
        if request.method not in ['PUT', 'PATCH', 'DELETE']:
            return True
        return request.user in obj.participants.all()


class IsParticipantOfConversation(permissions.BasePermission):
    """Allow only participants in a conversation to access messages"""
    def has_object_permission(self, request, view, obj):        
        # Check if user is authenticated
        if request.user.is_authenticated:
            return True

        # Check if the user is participant of the conversation
        if hasattr(obj, 'conversation') and request.user in obj.conversation.participants.all():
            return True

        return False
