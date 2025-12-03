from jwt.exceptions import ExpiredSignatureError

from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed

from .auth_token_manager import AuthTokenManager
from .tokens import decode_token


class TokenAuthentication(BaseAuthentication):
    __User = get_user_model()
    auth_manager = AuthTokenManager()

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
        try:
            payload = decode_token(token)
        except ExpiredSignatureError as e:
            raise AuthenticationFailed(str(e))

        self.__validate_payload(payload)

        try:
            user = self.__User.objects.get(id=payload['uid'])
        except self.__User.DoesNotExist:
            raise AuthenticationFailed('No such user')

        request.access_token = token
        request.access_token_payload = payload

        return user, None

    def authenticate_header(self, request):
        return f'Token: {settings.AUTHORIZATION_HEADER_PREFIX}'

    def __validate_payload(self, payload):
        if 'refresh' in payload and payload['refresh'] == True:
            raise AuthenticationFailed('Incorrect token')

        if 'uid' not in payload:
            raise AuthenticationFailed('Incorrect token')

        if 'jti' not in payload:
            raise AuthenticationFailed('Incorrect token')

        if not self.auth_manager.is_valid_token(payload['jti']):
            raise AuthenticationFailed('Incorrect token')
