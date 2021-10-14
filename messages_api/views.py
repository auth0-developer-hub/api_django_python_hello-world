from rest_framework.generics import RetrieveAPIView

from messages_api.models import Message
from messages_api.serializers import MessageSerializer


class MessageApiView(RetrieveAPIView):
    serializer_class = MessageSerializer
    text = None

    def get_object(self):
        return Message(text=self.text)


class PublicMessageApiView(MessageApiView):
    text = "The API doesn't require an access token to share this message."


class ProtectedMessageApiView(MessageApiView):
    text = "The API successfully validated your access token."


class AdminMessageApiView(MessageApiView):
    text = "The API successfully recognized you as an admin."
