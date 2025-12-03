from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from users.serializers import UserSerializer
from .auth_manager import AuthManager
from .serializers import LoginSerializer, RegirstrationSerializer


class LoginView(APIView):
    auth_manager = AuthManager()

    def post(self, request):
        login_data = LoginSerializer(data=request.data)

        if not login_data.is_valid():
            return Response({'message': login_data.errors}, status=status.HTTP_400_BAD_REQUEST)

        user = self.auth_manager.get_user(login_data.data['email'])
        if user is None:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(login_data.data['password']):
            return Response({'message': 'Wrong email or password'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(self.auth_manager.generate_tokens(user))


class RegistrationView(APIView):
    def post(self, request):
        registration_data = RegirstrationSerializer(data=request.data)

        if registration_data.is_valid():
            user = registration_data.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

        return Response({'message': registration_data.errors}, status=status.HTTP_400_BAD_REQUEST)
