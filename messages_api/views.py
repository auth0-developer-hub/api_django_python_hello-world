from rest_framework.generics import RetrieveAPIView

from messages_api.models import Message
from messages_api.serializers import MessageSerializer


class MessageApiView(RetrieveAPIView):
    serializer_class = MessageSerializer
    message = None

    def get_object(self):
        return Message(message=self.message)


class PublicMessageApiView(MessageApiView):
    message = "The API doesn't require an access token to share this message."



class AuthMessageApiView(MessageApiView):
    message = "The API successfully validated your access token."


class AdminMessageApiView(MessageApiView):
    message = "The API successfully recognized you as an admin."
