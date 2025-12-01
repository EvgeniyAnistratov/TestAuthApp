from django.contrib.auth import get_user_model
from rest_framework import serializers


class RegirstrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'middle_name', 'email', 'password']
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

