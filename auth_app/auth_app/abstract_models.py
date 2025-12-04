from django.db import models
from django.contrib.auth import get_user_model


class AbstractOwner(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_set')

    class Meta:
        abstract = True


class AbstractTimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractElement(AbstractOwner, AbstractTimeStamp):
    class Meta:
        abstract = True
