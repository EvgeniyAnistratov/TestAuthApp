from django.db import models


class UserManager(models.Manager):
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
                raise models.Model.DoesNotExist()

        except models.Model.DoesNotExist:
            return None

        return user
