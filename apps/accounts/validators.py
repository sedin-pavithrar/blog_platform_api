# Register User
# Store User in MongoDB
# Login
# Generate JWT
# Protected Routes
from rest_framework import serializers
from .models import User
import re


def validate_email(email):
    if User.objects(email=email).first():
        raise serializers.ValidationError("Email is already registered")
    return email


def validate_username(username):
    if User.objects(username=username).first():
        raise serializers.ValidationError("Username already taken")
    if not re.match(r"^[a-zA-Z0-9_]+$", username):
        raise serializers.ValidationError(
            "Username can contain only letters, numbers and underscores."
        )
    return username


def validate_password(value):
    if len(value) < 8:
        raise serializers.ValidationError("Password must be at least 8 characters.")

    if not re.search(r"[A-Z]", value):
        raise serializers.ValidationError("Password must contain one uppercase letter.")

    if not re.search(r"\d", value):
        raise serializers.ValidationError("Password must contain one number.")
    if not re.search(r"[a-z]", value):
        raise serializers.ValidationError("Password must contain one lowercase letter.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
        raise serializers.ValidationError(
            "Password must contain one special character."
        )

    return value
