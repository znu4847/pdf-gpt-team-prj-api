from rest_framework.serializers import ModelSerializer, ValidationError
from .models import User


class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "name",
            "email",
            "avatar",
        ]


class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "id",
            "password",
            "is_superuser",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "user_permissions",
            "groups",
        ]

    def validate_username(self, value):
        return value

    def validate(self, data):
        return data


class UserPasswordSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            "password",
        ]

    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError("Password is too short")
        return value
