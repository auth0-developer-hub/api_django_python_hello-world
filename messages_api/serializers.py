from rest_framework import serializers


class MetadataSerializer(serializers.Serializer):
    api = serializers.CharField()
    branch = serializers.CharField()


class MessageSerializer(serializers.Serializer):
    text = serializers.CharField()
    metadata = MetadataSerializer()
