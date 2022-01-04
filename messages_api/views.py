from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import exception_handler

from authz.permissions import HasAdminPermission
from messages_api.models import Message
from messages_api.serializers import MessageSerializer


class MessageApiView(RetrieveAPIView):
    serializer_class = MessageSerializer
    text = None

    def get_object(self):
        return Message(text=self.text)


class PublicMessageApiView(MessageApiView):
    text = "The secured API doesn't require an access token to share this public message."


class ProtectedMessageApiView(MessageApiView):
    text = "The secured API requires a valid access token to share this protected message."
    permission_classes = [IsAuthenticated]


class AdminMessageApiView(MessageApiView):
    text = "The secured API requires a valid access token and the read:admin-messages permission to share this admin message."
    permission_classes = [IsAuthenticated, HasAdminPermission]


def api_exception_handler(exc, context=None):
    response = exception_handler(exc, context=context)
    if response.status_code == 403:
        response.data = {
            'error': 'insufficient_permissions',
            'error_description': response.data.get('detail', 'API Error'),
            'message': 'Permission denied'
        }
    elif response and isinstance(response.data, dict):
        response.data = {'message': response.data.get('detail', 'API Error')}
    else:
        response.data = {'message': 'API Error'}
    return response
