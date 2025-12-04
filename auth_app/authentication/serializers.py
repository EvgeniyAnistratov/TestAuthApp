from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class RefreshSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(required=True)


class RegirstrationSerializer(serializers.ModelSerializer):
    repeat_password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'middle_name', 'email', 'password', 'repeat_password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model()(
            first_name=validated_data.get('first_name', None),
            last_name=validated_data.get('last_name', None),
            middle_name=validated_data.get('middle_name', None),
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    def validate(self, attrs):
        errors = dict()
        password = attrs.get('password')

        if attrs.get('repeat_password') != password:
            errors['repeat_password'] = 'repeat_password must be equil to password'

        try:
            validate_password(password=password)
        except ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super().validate(attrs)
