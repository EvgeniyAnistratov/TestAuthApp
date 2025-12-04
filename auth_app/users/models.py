from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

from authorization.models import Role
from .model_managers import UserManager
from .utils import make_password, compare_passwords


class User(AbstractBaseUser):
    objects = UserManager()

    first_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    last_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    middle_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    email = models.EmailField(unique=True, blank=False)
    is_active = models.BooleanField(default=True)

    roles = models.ManyToManyField(Role, through='UserRole')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        return compare_passwords(raw_password, self.password)

    @property
    def roles_list(self):
        return [role.name for role in self.roles.all()]

    def soft_delete(self):
        self.is_active = False
        self.save()


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'role')
