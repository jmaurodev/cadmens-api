from rest_framework import viewsets
from rest_framework import permissions
from app.models import Message
from app.serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    """
    Allows messages to be managed.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]