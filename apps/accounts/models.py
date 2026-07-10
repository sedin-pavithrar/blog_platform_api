from datetime import datetime

from mongoengine import Document, StringField, EmailField, BooleanField, DateTimeField


class User(Document):
    username = StringField(required=True, unique=True, min_length=3, max_length=50)
    full_name = StringField(required=True, max_length=100)

    email = EmailField(required=True, unique=True)

    password = StringField(
        required=True,
    )
    role = StringField(choices=("ADMIN", "AUTHOR"), default="AUTHOR")
    is_active = BooleanField(default=True)

    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        "collection": "users",
        "indexes": ["username", "email", "role"],
        "ordering": ["-created_at"],
    }

    def __str__(self):
        return self.username

    # MongoEngine doesn't automatically update on every save so overriding save() method
    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        return super().save(*args, **kwargs)
