from django.contrib.auth.hashers import make_password, check_password
from .models import User


def register_user(validated_data: dict) -> User:
    """
    Register a new user.

    Hashes the user's password before saving
    the user document to MongoDB.
    """

    user = User(
        username=validated_data["username"],
        full_name=validated_data["full_name"],
        email=validated_data["email"],
        password=make_password(validated_data["password"]),
    )

    user.save()
    return user


def login_user(email: str, password: str) -> User:
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        raise ValueError("Invalid Email or Password")

    if not user.is_active:
        raise ValueError("Account is disabled.")

    if not check_password(password, user.password):
        raise ValueError("Invalid Email or Password")

    return user


# def login_user(email: str, password: str):

#     print("Email received:", email)
#     print("Password received:", password)

#     try:
#         user = User.objects.get(email=email)
#         print("User Found:", user.email)
#         print("Stored Password:", user.password)

#     except User.DoesNotExist:
#         print("User not found")
#         raise ValueError("Invalid Email or Password")

#     print("Password Match:", check_password(password, user.password))

#     if not check_password(password, user.password):
#         raise ValueError("Invalid Email or Password")

#     return user

# def login_user(email: str, password: str) -> User:

#     print("=" * 50)
#     print("Login Attempt")
#     print("Email:", email)
#     print("Password:", password)

#     try:
#         user = User.objects.get(email=email)
#         print("User found:", user.email)
#         print("Stored password:", user.password)

#     except User.DoesNotExist:
#         print("User does not exist")
#         raise ValueError("Invalid Email or Password")

#     print("Password matches:", check_password(password, user.password))

#     if not check_password(password, user.password):
#         raise ValueError("Invalid Email or Password")

#     print("Is Active:", user.is_active)

#     return user
