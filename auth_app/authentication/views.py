from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authentication import get_authorization_header
from rest_framework.views import APIView
from rest_framework.response import Response

from users.serializers import UserSerializer
from .auth_token_manager import AuthTokenManager, InvalidRefreshToken
from .serializers import LoginSerializer, RegirstrationSerializer, RefreshSerializer


class LoginView(APIView):
    auth_manager = AuthTokenManager()
    authentication_classes = []

    __User = get_user_model()

    def post(self, request):
        login_data = LoginSerializer(data=request.data)

        if not login_data.is_valid():
            return Response({'message': login_data.errors}, status=status.HTTP_400_BAD_REQUEST)

        user = self.__User.objects.get_user_or_none(email=login_data.data['email'])
        if user is None:
            return Response({'message': 'No such user'}, status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(login_data.data['password']):
            return Response({'message': 'Wrong email or password'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(self.auth_manager.generate_tokens(user))


class LogoutView(APIView):
    auth_manager = AuthTokenManager()

    def post(self, request):
        if hasattr(request, 'access_token'):
            token = getattr(request, 'access_token')
        else:
            header = get_authorization_header(request)
            token = header.replace(settings.AUTHORIZATION_HEADER_PREFIX, '').strip()

        payload = getattr(request, 'access_token_payload') if hasattr(request, 'access_token_payload') else None

        self.auth_manager.disable_atoken(token, payload)
        self.auth_manager.disable_rtoken(self.request.user.id)

        return Response()


class RefreshTokenView(APIView):
    auth_manager = AuthTokenManager()
    authentication_classes = []

    __User = get_user_model()

    def post(self, requeset):
        refresh_data = RefreshSerializer(data=requeset.data)

        if not refresh_data.is_valid():
            return Response({'message': refresh_data.errors}, status=status.HTTP_400_BAD_REQUEST)

        token = refresh_data.data['refresh_token']
        try:
            payload = self.auth_manager.decode_rtoken(token)
        except InvalidRefreshToken as e:
            return Response({'message': str(e)}, status=status.HTTP_401_UNAUTHORIZED)

        user = self.__User.objects.get_user_or_none(user_id=payload['uid'])
        if user is None:
            return Response({'message': 'No such user'}, status=status.HTTP_404_NOT_FOUND)

        try:
            new_tokens = self.auth_manager.refresh_tokens(user, payload['jti'], token, payload['exp'])
        except InvalidRefreshToken as e:
            return Response({'message': str(e)}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(new_tokens)


class RegistrationView(APIView):
    authentication_classes = []

    def post(self, request):
        registration_data = RegirstrationSerializer(data=request.data)

        if registration_data.is_valid():
            user = registration_data.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

        return Response({'message': registration_data.errors}, status=status.HTTP_400_BAD_REQUEST)
