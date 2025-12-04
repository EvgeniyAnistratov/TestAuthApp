from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response

from authorization.permissions import SpecificElementPermission
from .serializers import UserSerializer


class GenericUserView(generics.RetrieveUpdateAPIView):
    __User = get_user_model()

    permission_classes = [SpecificElementPermission]
    queryset = __User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
