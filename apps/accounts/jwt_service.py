# generate_tokens(user)
#         │
#         ├── access token
#         └── refresh token

import jwt
from datetime import datetime, timezone
from django.conf import settings


def generate_access_token(user):
    now = datetime.now(timezone.utc)
    simple_jwt_settings = getattr(settings, "SIMPLE_JWT", {})

    payload = {
        "user_id": str(user.id),
        "username": user.username,
        "email": user.email,
        "role": user.role,
        "iat": now,
        "exp": now + simple_jwt_settings.get("ACCESS_TOKEN_LIFETIME"),
        "type": "access",
    }

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=simple_jwt_settings.get("ALGORITHM", "HS256"),
    )


def generate_refresh_token(user):
    now = datetime.now(timezone.utc)
    simple_jwt_settings = getattr(settings, "SIMPLE_JWT", {})

    payload = {
        "user_id": str(user.id),
        "iat": now,
        "exp": now + simple_jwt_settings.get("REFRESH_TOKEN_LIFETIME"),
        "type": "refresh",
    }
    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=simple_jwt_settings.get("ALGORITHM", "HS256"),
    )
