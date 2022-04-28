# -*- coding: utf-8 -*-
from django.db import models


class Message(models.Model):
    PRECEDENCE = (
        (1, 'Urgentíssima'),
        (2, 'Urgente'),
        (3, 'Preferencial'),
        (4, 'Rotina'),
    )
    CONFIDENTIALITY = (
        (1, 'Ultra-Secreto'),
        (2, 'Secreto'),
        (3, 'Confidencial'),
        (4, 'Reservado'),
        (5, 'Ostensivo'),
    )
    ENCRYPTION = (
        (False, 'Claro'),
        (True, 'Criptografado'),
    )
    NETWORK = (
        (1, 'Comando'),
        (2, 'Operações'),
        (3, 'Logística'),
    )
    ENVIRONMENT = (
        (1, 'Rádio'),
        (2, 'Telefone'),
        (3, 'Digital'),
        (4, 'Mensageiro'),
    )

    content = models.CharField(max_length=100)
    encryption = models.BooleanField(choices=ENCRYPTION)
    network = models.CharField(max_length=1, choices=NETWORK)
    environment = models.CharField(max_length=1, choices=ENVIRONMENT)
    precedence = models.CharField(max_length=1, choices=PRECEDENCE)
    confidentiality = models.CharField(max_length=1, choices=CONFIDENTIALITY)
    sender_nickname = models.ForeignKey(
        'Nickname', on_delete=models.PROTECT, related_name='+'
    )
    receiver_nickname = models.ForeignKey(
        'Nickname', on_delete=models.PROTECT, related_name='+'
    )
    sender_organization = models.ForeignKey(
        'Organization', on_delete=models.PROTECT, related_name='+'
    )
    receiver_organization = models.ForeignKey(
        'Organization', on_delete=models.PROTECT, related_name='+'
    )

    def __str__(self):
        id = self.id
        head = self.content[:10]
        tail = self.content[-10:]
        return f'ID: {id}| Content: {head} (...) {tail}'


class Network(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Environment(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Nickname(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
