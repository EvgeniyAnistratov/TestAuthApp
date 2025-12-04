from django.db.models import Prefetch
from django.contrib.auth import get_user_model

from rest_framework.permissions import BasePermission

from authorization.enums import ElementEnum, RoleEnum
from authorization.models import Element, Permission


class WrongMethod(Exception):
    pass


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user is None:
            return False

        return request.user.roles.filter(name=RoleEnum.ADMIN.value).exists()


class SpecificElementPermission(BasePermission):
    __User = get_user_model()

    def has_object_permission(self, request, view, obj):
        if request.user is None:
            return False

        element = Element.objects.filter(specificelement__name='{}.{}'.format(obj._meta.app_label, obj._meta.model_name))

        if len(element) == 0:
            return False

        roles = request.user.roles.prefetch_related(
            Prefetch('element_permissions', queryset=Permission.objects.filter(element=element[0]))
        )
        permissions = []
        for r in roles:
            permissions += r.element_permissions.all()

        try:
            part = self.__get_part_fieldname(request.method)
        except WrongMethod:
            return False

        owner_permission = any([getattr(p, f'{part}_permission') for p in permissions])
        all_permission = any([getattr(p, f'{part}_all_permission') for p in permissions])

        return all_permission if all_permission else owner_permission and self.check_owner(obj, request.user, element[0])

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
