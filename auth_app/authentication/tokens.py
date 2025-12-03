import jwt
import datetime
from datetime import timezone
from uuid import uuid1

from django.conf import settings


_ALGORITHM = 'HS256'


def get_access_token(user_id: int, roles: list[str]):
    payload = {
        'exp': datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(seconds=settings.JWT_ACCESS_TTL),
        'uid': user_id,
        'roles': roles,
        'jti': str(uuid1()),
    }
    return jwt.encode(payload=payload, key=settings.JWT_SECRET_KEY, algorithm=_ALGORITHM)


def get_refresh_token(user_id: int):
    payload = {
        'exp': datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(seconds=settings.JWT_REFRESH_TTL),
        'uid': user_id,
        'jti': str(uuid1()),
    }
    return jwt.encode(payload=payload, key=settings.JWT_SECRET_KEY, algorithm=_ALGORITHM)


def decode_token(token):
    return jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[_ALGORITHM])
