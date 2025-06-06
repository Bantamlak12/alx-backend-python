from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsParticipantOfConversation


class ConversationViewSet(viewsets.ModelViewSet):
    """Only authenticated users and participants can access conversation"""
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes  = [IsAuthenticated, IsParticipantOfConversation]

    filter_backends = [filters.SearchFilter]
    search_fields = ['participants__email']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessageViewSet(viewsets.ModelViewSet):
    """Only participants of a conversation can send, view, update, and delete a message"""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['sent_at']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        message = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
