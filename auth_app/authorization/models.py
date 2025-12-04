from django.db import models


class Element(models.Model):
    name = models.CharField(max_length=128, unique=True)


class Role(models.Model):
    name = models.CharField(max_length=128, unique=True)


class Permission(models.Model):
    element = models.ForeignKey(Element, on_delete=models.CASCADE, related_name='role_permissions')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='element_permissions')

    read_permission = models.BooleanField(default=False)
    read_all_permission = models.BooleanField(default=False)
    create_permission = models.BooleanField(default=False)
    update_permission = models.BooleanField(default=False)
    update_all_permission = models.BooleanField(default=False)
    delete_permission = models.BooleanField(default=False)
    delete_all_permission = models.BooleanField(default=False)


class SpecificElement(models.Model):
    name = models.CharField(max_length=254, unique=True)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
