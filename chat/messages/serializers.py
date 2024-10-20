from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Message


class ListSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = [
            "pk",
            "conversation",
            "type",
            "text",
            "timestamp",
        ]


class CreateSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = [
            "conversation",
            "type",
            "text",
        ]
