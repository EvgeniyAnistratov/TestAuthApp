import bcrypt

from django.conf import settings


def make_password(raw_password):
    byte_password = raw_password.encode(settings.STR_ENCODING)
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(byte_password, salt).decode(settings.STR_ENCODING)


def compare_passwords(provided_password, hashed_password):
    return bcrypt.checkpw(
        provided_password.encode(settings.STR_ENCODING),
        hashed_password.encode(settings.STR_ENCODING)
    )
