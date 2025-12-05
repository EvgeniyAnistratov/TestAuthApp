from django.db.models import Prefetch
from rest_framework.permissions import BasePermission

from .enums import ElementEnum, RoleEnum
from .models import Element, Permission


class WrongMethod(Exception):
    pass


class MissedRequiredAttribute(Exception):
    pass


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user is None:
            return False

        return request.user.roles.filter(name=RoleEnum.ADMIN.value).exists()


class PermissionMixin:
    def load_element(self, model):
        elements = Element.objects.filter(specificelement__name='{}.{}'.format(model._meta.app_label, model._meta.model_name))
        return elements[0] if len(elements) else None

    def load_permissions(self, user, element):
        roles = user.roles.prefetch_related(
            Prefetch('element_permissions', queryset=Permission.objects.filter(element=element))
        )

        permissions = []
        for r in roles:
            permissions += r.element_permissions.all()

        return permissions


class PermissionForModelMixin(PermissionMixin):
    def get_permission_field(self):
        raise NotImplementedError()

    def has_permission(self, request, view):
        if not hasattr(view, 'permission_for_model'):
            raise MissedRequiredAttribute('permission_for_model attribute is missed')

        if request.user is None:
            return False

        element = self.load_element(getattr(view, 'permission_for_model'))
        if element is None:
            return False

        permissions = self.load_permissions(request.user, element)

        return any([getattr(p, self.get_permission_field()) for p in permissions])


class CreatePermission(PermissionForModelMixin, BasePermission):
    def get_permission_field(self):
        return 'create_permission'

    def has_permission(self, request, view):
        if request.method != 'POST':
            return True  # Allow other methods

        return super().has_permission(request, view)


class ReadAllPermission(PermissionForModelMixin, BasePermission):
    def get_permission_field(self):
        return 'read_all_permission'

    def has_permission(self, request, view):
        if request.method != 'GET':
            return True  # Allow other methods

        return super().has_permission(request, view)


class SpecificElementPermission(PermissionMixin, BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user is None:
            return False

        element = self.load_element(obj)
        if element is None:
            return False

        permissions = self.load_permissions(request.user, element)

        try:
            part = self.__get_part_fieldname(request.method)
        except WrongMethod:
            return False

        owner_permission = any([getattr(p, f'{part}_permission') for p in permissions])
        all_permission = any([getattr(p, f'{part}_all_permission') for p in permissions])

        return all_permission if all_permission else owner_permission and self.check_owner(obj, request.user, element)

    def __get_part_fieldname(self, method):
        if method == 'GET':
            return 'read'
        elif method == 'DELETE':
            return 'delete'
        elif method in ['PUT', 'PATCH', 'POST']:
            return 'update'
        else:
            raise WrongMethod()

    def check_owner(self, obj, user, element):
        return user.id == obj.id if element.name == ElementEnum.USER.value else obj.owner.id == user.id
