from django.conf import settings
from redis import Redis


class RedisTokenManager:
    USER_KEY = 'USER:{}'

    def __init__(self, db_id):
        self.redis = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=db_id)

    def format_user_key(self, user_id):
        return self.USER_KEY.format(user_id)

    def get_key(self, key):
        return self.redis.get(key)

    def get_del_key(self, key):
        return self.redis.getdel(key)

    def set_key(self, key, value, exat=None):
        self.redis.set(key, value, exat=exat)

    def delete_key(self, key):
        self.redis.delete(key)

    def write_rtoken(self, user_id, jti, token, exat):
        self.redis.set(self.USER_KEY.format(user_id), jti, exat=exat)
        self.redis.set(jti, token, exat=exat)

    def get_existed_rtoken(self, user_id: int):
        jti = self.redis.get(self.USER_KEY.format(user_id))
        return self.redis.get(jti) if jti else None
