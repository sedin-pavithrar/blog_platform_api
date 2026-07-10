from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .services import (
    register_user,
    login_user,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .jwt_service import generate_access_token, generate_refresh_token


class RegisterAPIView(APIView):
    """
    API endpoint to Register new user
    """

    def post(self, request):
        """
        Step 1
        Client sends request POST /api/register


        """

        request_serializer = RegisterSerializer(data=request.data)  # creates serializer

        # if not serializer.is_valid():
        #     return Response(
        #         serializer.errors,
        #         status = status.HTTP_400_BAD_Request,
        #     ) # validate email username password

        request_serializer.is_valid(raise_exception=True)
        user = register_user(request_serializer.validated_data)

        response_serializer = UserSerializer(
            user
        )  # Serialize response removes password and formats output

        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED,
        )


class LoginAPIView(APIView):
    """
    API endpoint to Authenticate  a user
    """

    def post(self, request):
        request_serializer = LoginSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        try:
            user = login_user(
                request_serializer.validated_data["email"],
                request_serializer.validated_data["password"],
            )

        except ValueError as e:
            return Response(
                {"message": str(e)},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)
        response_serializer = UserSerializer(user)

        return Response(
            {
                "access": access_token,
                "refresh": refresh_token,
                "user": response_serializer.data,
            },
            status=status.HTTP_200_OK,
        )
