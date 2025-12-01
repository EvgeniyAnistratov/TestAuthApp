from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import RegirstrationSerializer
from users.serializers import UserSerializer


class RegistrationView(APIView):

    def post(self, request):
        registration_data = RegirstrationSerializer(data=request.data)

        if registration_data.is_valid():
            user = registration_data.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

        return Response({'message': registration_data.errors}, status=status.HTTP_400_BAD_REQUEST)
