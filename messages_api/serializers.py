from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    text = serializers.CharField()
    api = serializers.CharField()
    branch = serializers.CharField()
