from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Conversation


class ListSerializer(ModelSerializer):
    class Meta:
        model = Conversation
        fields = [
            "pk",
            "title",
            "pdf_url",
            "embed_url",
            "last_message",
        ]


class DetailSerializer(ModelSerializer):
    class Meta:
        model = Conversation
        fields = "__all__"


class CreateSerializer(ModelSerializer):
    class Meta:
        model = Conversation
        fields = [
            "pk",
            "user",
            "title",
            "pdf_url",
            "embed_url",
        ]

    def validate_name(self, value):
        return value

    def validate(self, data):
        return data
