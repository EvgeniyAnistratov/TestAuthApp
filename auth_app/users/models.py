import bcrypt

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    last_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    middle_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    email = models.EmailField(unique=True, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["email"]

    def set_password(self, raw_password):
        byte_password = raw_password.encode('utf-8')
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(byte_password, salt)
        self._password = raw_password
