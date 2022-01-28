from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import exception_handler

from messages_api.models import Message
from messages_api.serializers import MessageSerializer


class MessageApiView(RetrieveAPIView):
    serializer_class = MessageSerializer
    text = None

    def get_object(self):
        return Message(text=self.text)


class PublicMessageApiView(MessageApiView):
    text = "This is a public message."


class ProtectedMessageApiView(MessageApiView):
    text = "This is a protected message."
    permission_classes = [IsAuthenticated]


class AdminMessageApiView(MessageApiView):
    text = "This is an admin message."
    permission_classes = [IsAuthenticated]


def api_exception_handler(exc, context=None):
    response = exception_handler(exc, context=context)
    if response and isinstance(response.data, dict):
        response.data = {'message': response.data.get('detail', 'API Error')}
    else:
        response.data = {'message': 'API Error'}
    return response
