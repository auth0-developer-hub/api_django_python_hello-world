from rest_framework.generics import RetrieveAPIView

from messages_api.models import Message
from messages_api.serializers import MessageSerializer


class MessageApiView(RetrieveAPIView):
    serializer_class = MessageSerializer
    text = None

    def get_object(self):
        return Message(text=self.text)


class PublicMessageApiView(MessageApiView):
    text = "The starter API doesn't require an access token to share this public message."


class ProtectedMessageApiView(MessageApiView):
    text = "The starter API doesn't require an access token to share this protected message."


class AdminMessageApiView(MessageApiView):
    text = "The starter API doesn't require an access token to share this admin message."
