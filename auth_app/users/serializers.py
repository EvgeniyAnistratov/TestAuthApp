from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'email']
        extra_kwargs = {'id': {'read_only': True}}


class UserRolesSerializer(serializers.Serializer):
    roles = serializers.ListField(child=serializers.IntegerField(min_value=1))
