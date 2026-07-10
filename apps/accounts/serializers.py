from rest_framework import serializers
from .validators import validate_email, validate_username, validate_password


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=50,
        validators=[validate_username],
    )

    full_name = serializers.CharField(max_length=100)

    email = serializers.EmailField(
        validators=[validate_email],
    )

    password = serializers.CharField(
        write_only=True,
        min_length=8,
        style={"input_type": "password"},
        validators=[validate_password],
    )


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class UserSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()

    username = serializers.CharField()

    full_name = serializers.CharField()

    email = serializers.EmailField()

    role = serializers.CharField()

    created_at = serializers.DateTimeField()

    updated_at = serializers.DateTimeField()

    def get_id(self, obj):
        return str(obj.id)
