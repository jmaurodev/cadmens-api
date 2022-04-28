# -*- coding: utf-8 -*-
from rest_framework import serializers
from app.models import Message


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
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
