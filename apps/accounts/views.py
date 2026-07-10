from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .services import (
    register_user,
    login_user,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


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

        # if not serializer.is_valid():
        #     return Response(
        #         serializer.errors,
        #         status = status.HTTP_400_BAD_REQUEST,
        #     )

        request_serializer.is_valid(raise_exception=True)
        user = login_user(
            request_serializer.validated_data["email"],
            request_serializer.validated_data["password"],
        )

        response_serializer = UserSerializer(user)

        return Response(
            response_serializer.data,
            status=status.HTTP_200_OK,
        )
