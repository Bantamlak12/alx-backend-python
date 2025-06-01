from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ViewSet):

    def list(self, request):
        user_id = request.query_params.get('user_id')
        queryset = Conversation.objects.all()

        if user_id:
            queryset = queryset.filter(participants_user_id=user_id)

        serializer = ConversationSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ConversationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageViewSet(viewsets.ViewSet):

    def list(self, request):
        conversation_id = request.query_params.get('conversation_id')
        queryset = Message.objects.all()

        if conversation_id:
            queryset = queryset.filter(conversation__conversation_id=conversation_id)

        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.save()
            return Response(MessageSerializer(message), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
