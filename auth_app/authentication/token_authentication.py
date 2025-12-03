from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed

from .tokens import decode_token


class TokenAuthentication(BaseAuthentication):
    _User = get_user_model()

    def authenticate(self, request):
        auth_header = get_authorization_header(request)

        if isinstance(auth_header, bytes):
            auth_header = auth_header.decode(settings.STR_ENCODING)
        elif isinstance(auth_header, str):
            auth_header = auth_header
        else:
            raise AuthenticationFailed('Broken authorization header')

        if not auth_header.startswith(settings.AUTHORIZATION_HEADER_PREFIX):
            raise AuthenticationFailed('Broken authorization header')

        token = auth_header.replace(settings.AUTHORIZATION_HEADER_PREFIX, '').strip()
        payload = decode_token(token)

        if 'uid' not in payload:
            raise AuthenticationFailed('Incorrect token')

        try:
            user = self._User.objects.get(id=payload['uid'])
        except self._User.DoesNotExist:
            raise AuthenticationFailed('No such user')

        return user, None

    def authenticate_header(self, request):
        return f'Token: {settings.AUTHORIZATION_HEADER_PREFIX}'
