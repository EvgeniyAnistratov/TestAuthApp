AUTHORIZATION_HEADER_PREFIX = 'Bearer'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'authentication.token_authentication.TokenAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [],
    'UNAUTHENTICATED_USER': None,
}