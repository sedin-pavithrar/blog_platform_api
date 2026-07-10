from mongoengine import connect
from decouple import config


def initialize_database():
    connect(
        host=config("MONGODB_URI", default="mongodb://localhost:27017/blog_platform")
    )
