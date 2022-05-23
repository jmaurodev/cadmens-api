# -*- coding: utf-8 -*-
from rest_framework import viewsets, filters
from rest_framework import permissions
from app import models
from app import serializers
from django_filters.rest_framework import DjangoFilterBackend


class BaseModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ['name']
    search_fields = ['name']


class MessageViewSet(BaseModelViewSet):
    """
    Allows messages to be managed.
    """

    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    ordering_fields = '__all__'
    search_fields = ['content']


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


class NicknameViewSet(BaseModelViewSet):
    """
    Allow nicknames to be managed.
    """

    queryset = models.Nickname.objects.all()
    serializer_class = serializers.NicknameSerializer


class OrganizationViewSet(BaseModelViewSet):
    """
    Allow organizations to be managed.
    """

    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
