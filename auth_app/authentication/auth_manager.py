from django.contrib.auth import get_user_model

from .redis_token_manager import RedisTokenManager
from .tokens import get_access_token, get_refresh_token


class AuthManager:
    _User = get_user_model()
    blacklist: RedisTokenManager = RedisTokenManager(1)
    token_store: RedisTokenManager = RedisTokenManager(2)

    def get_user(self, email: str):
        try:
            user = self._User.objects.get(email=email)

            if not user.is_active:
                raise self._User.DoesNotExist()

        except self._User.DoesNotExist:
            return None

        return user

    def generate_tokens(self, user):
        atoken, _ = get_access_token(user.id, list(user.roles.values_list('name', flat=True)))
        existed_rtoken = self.token_store.get_existed_rtoken(user.id)

        if existed_rtoken:
            rtoken = existed_rtoken
        else:
            rtoken, rpayload = get_refresh_token(user.id)
            self.token_store.write_rtoken(user.id, rpayload['jti'], rtoken, rpayload['exp'])

        return {
            'access_token': atoken,
            'refresh_token': rtoken,
        }
