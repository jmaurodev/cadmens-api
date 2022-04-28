# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework import permissions
from app.models import Message, Network
from app.serializers import MessageSerializer, NetworkSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """
    Allows messages to be managed.
    """

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]


class NetworkViewSet(viewsets.ModelViewSet):
    """
    Allow networks to be managed.
    """

    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [permissions.IsAuthenticated]
