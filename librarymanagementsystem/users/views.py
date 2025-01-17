from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics
# from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import IsLibrarian, IsMember
from .serializers import (UserDeactivateSerializer, UserRegistrationSerializer,
                          UserLoginSerializer)

User = get_user_model()


class UserRegistrationView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            name = serializer.validated_data['name']
            role = serializer.validated_data['role']
            password = serializer.validated_data['password']

            user = User.objects.create(
                username=username,
                name=name,
                role=role
            )

            user.set_password(password)
            user.save()

            content = {
                'username': user.username,
                'name': user.name,
                'role': user.role
            }

            response_content = {
                'status': True,
                'message': 'User registered successfully.',
                'result': content
            }

            return Response(response_content, status=status.HTTP_200_OK)

        else:

            response_content = {
                'status': True,
                'message': 'Unable to create user.',
                'result': serializer.errors
            }

            return Response(response_content, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = User.objects.get(username=username)

            # token, created = Token.objects.get_or_create(user=user)
            token = RefreshToken.for_user(user)
            content = {
                'username': user.username,
                'name': user.name,
                'role': user.role,
                'token': {
                    'refresh': str(token),
                    'access': str(token.access_token)
                },
            }

            response_content = {
                'status': True,
                'message': 'User logged in successfully.',
                'result': content
            }

            return Response(response_content, status=status.HTTP_200_OK)

        else:

            response_content = {
                'status': False,
                'message': 'Unable to login user.',
                'result': serializer.errors
            }

            return Response(response_content, status=status.HTTP_400_BAD_REQUEST)


class UserDeactivateView(APIView):
    permission_classes = (IsAuthenticated, IsMember)
    serializer_class = UserDeactivateSerializer

    def delete(self, request, id):
        user_data = {
            'user_id': id
        }
        serializer = self.serializer_class(data=user_data)

        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']

            user = User.objects.get(id=user_id)

            user.is_active = False
            user.save()

            response_content = {
                'status': True,
                'message': 'User deactivated successfully.'
            }

            return Response(response_content, status=status.HTTP_200_OK)

        else:

            response_content = {
                'status': False,
                'message': 'Unable to deactivate user.',
                'result': serializer.errors
            }

            return Response(response_content, status=status.HTTP_400_BAD_REQUEST)



