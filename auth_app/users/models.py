from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    last_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    middle_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    email = models.EmailField(unique=True, blank=False)

    REQUIRED_FIELDS = ["email"]
