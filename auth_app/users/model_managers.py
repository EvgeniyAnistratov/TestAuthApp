from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Manager


class UserManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def get_user_or_none(self, user_id=None, email=None):
        if user_id is None and email is None:
            raise Exception('one parameter must be filled in')

        try:
            params = {}

            if user_id:
                params['id'] = user_id
            if email:
                params['email'] = email

            user = self.get(**params)

            if not user.is_active:
                raise ObjectDoesNotExist()

        except ObjectDoesNotExist:
            return None

        return user
