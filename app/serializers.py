# -*- coding: utf-8 -*-
from rest_framework import serializers
from app import models


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Message
        fields = (
            'content',
            'encryption',
            'network',
            'environment',
            'precedence',
            'confidentiality',
            'sender_nickname',
            'receiver_nickname',
            'sender_organization',
            'receiver_organization',
            'id',
        )


class NetworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Network
        fields = (
            'name',
            'id',
        )


class EnvironmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Network
        fields = (
            'name',
            'id',
        )


class NicknameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Nickname
        fields = (
            'name',
            'id',
        )


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Organization
        fields = (
            'name',
            'id',
        )
