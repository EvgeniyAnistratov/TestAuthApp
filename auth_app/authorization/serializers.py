from rest_framework import serializers

from .models import Element, Permission, Role


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = ['id', 'name']
        extra_kwargs = {'id': {'read_only': True}}


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']
        extra_kwargs = {'id': {'read_only': True}}


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'element': {'read_only': True},
            'role': {'read_only': True},
        }
