from rest_framework.generics import ListAPIView

from .models import Element, Permission, Role
from .permissions import IsAdmin
from .serializers import ElementSerializer, PermissionSerializer, RoleSerializer


class ElementListView(ListAPIView):
    permission_classes = [IsAdmin]
    queryset = Element.objects.all()
    serializer_class = ElementSerializer


class PermissionListView(ListAPIView):
    authentication_classes = []
    permission_classes = [IsAdmin]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    def filter_queryset(self, queryset):
        element_id = self.request.query_params.get('element_id')
        role_id = self.request.query_params.get('role_id')

        params = {}
        if element_id:
            params['element_id'] = element_id
        if role_id:
            params['role_id'] = role_id

        return super().filter_queryset(queryset).filter(**params)


class RoleListView(ListAPIView):
    permission_classes = [IsAdmin]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
