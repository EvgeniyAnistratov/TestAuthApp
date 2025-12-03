from django.contrib.auth import get_user_model

from .tokens import get_access_token, get_refresh_token


class AuthManager:
    _User = get_user_model()

    def get_user(self, email: str):
        try:
            user = self._User.objects.get(email=email)

            if not user.is_active:
                raise self._User.DoesNotExist()

        except self._User.DoesNotExist:
            return None

        return user

    def generate_tokens(self, user):
        return {
            'access_token': get_access_token(user.id, list(user.roles.values_list('name', flat=True))),
            'refresh_token': get_refresh_token(user.id)
        }
