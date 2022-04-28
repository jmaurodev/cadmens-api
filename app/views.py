# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework import permissions
from app import models
from app import serializers


class BaseModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]


class MessageViewSet(BaseModelViewSet):
    """
    Allows messages to be managed.
    """

    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer


class NetworkViewSet(BaseModelViewSet):
    """
    Allow networks to be managed.
    """

    queryset = models.Network.objects.all()
    serializer_class = serializers.NetworkSerializer


class EnvironmentViewSet(BaseModelViewSet):
    """
    Allow environments to be managed.
    """

    queryset = models.Environment.objects.all()
    serializer_class = serializers.EnvironmentSerializer
