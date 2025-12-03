from django.contrib.auth import get_user_model

from .redis_token_manager import RedisTokenManager
from .tokens import get_access_token, get_refresh_token, decode_token


class AuthTokenManager:
    __User = get_user_model()
    blacklist: RedisTokenManager = RedisTokenManager(1)
    whitelsit: RedisTokenManager = RedisTokenManager(2)

    def get_user(self, email: str):
        try:
            user = self.__User.objects.get(email=email)

            if not user.is_active:
                raise self.__User.DoesNotExist()

        except self.__User.DoesNotExist:
            return None

        return user

    def generate_tokens(self, user):
        atoken, _ = get_access_token(user.id, list(user.roles.values_list('name', flat=True)))
        existed_rtoken = self.whitelsit.get_existed_rtoken(user.id)

        if existed_rtoken:
            rtoken = existed_rtoken
        else:
            rtoken, rpayload = get_refresh_token(user.id)
            self.whitelsit.write_rtoken(user.id, rpayload['jti'], rtoken, rpayload['exp'])

        return {
            'access_token': atoken,
            'refresh_token': rtoken,
        }

    def disable_atoken(self, token, payload=None):
        _payload = payload if payload else decode_token(token)
        jti = _payload['jti']
        self.blacklist.set_key(jti, token, _payload['exp'])

    def disable_rtoken(self, user_id):
        user_key = self.whitelsit.format_user_key(user_id)
        jti = self.whitelsit.get_del_key(user_key)

        if jti:
            token = self.whitelsit.get_del_key(jti)
            payload = decode_token(token)
            self.blacklist.set_key(jti, token, payload['exp'])

    def is_valid_token(self, jti):
        return self.blacklist.get_key(jti) is None
