from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from authorization.models import Role
from authorization.permissions import IsAdmin, SpecificElementPermission
from .serializers import UserSerializer, UserRolesSerializer


USER = get_user_model()


class GenericUserView(generics.RetrieveUpdateAPIView):
    permission_classes = [SpecificElementPermission]
    queryset = USER.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserChangeRoleMixin:
    adding = True

    def change_roles(self, request, pk):
        user = get_object_or_404(USER.objects.prefetch_related('roles'), id=pk)
        user_roles_serializer = UserRolesSerializer(data=request.data)

        if user_roles_serializer.is_valid():
            roles_ids = user_roles_serializer.data['roles']
            roles = Role.objects.filter(id__in=roles_ids)

            if len(roles) != len(roles_ids):
                return Response({'roles': 'contains non-existen identifiers'}, status=status.HTTP_400_BAD_REQUEST)

            if self.adding:
                user.add_roles(roles)
            else:
                user.delete_roles(roles)

        return Response(status=status.HTTP_200_OK)

class UserAddRolesView(UserChangeRoleMixin, APIView):
    permission_classes = [IsAdmin]

    def post(self, request, pk, *args, **kwargs):
        return self.change_roles(request, pk)


class UserDeleteRolesView(UserChangeRoleMixin, APIView):
    permission_classes = [IsAdmin]
    adding = False

    def post(self, request, pk, *args, **kwargs):
        return self.change_roles(request, pk)
