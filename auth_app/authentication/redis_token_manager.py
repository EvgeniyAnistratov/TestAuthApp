from django.conf import settings
from redis import Redis


class RedisTokenManager:
    def __init__(self, db_id):
        self.redis = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=db_id)

    def get_token(self, jti):
        return self.redis.get(jti)

    def write_rtoken(self, user_id, jti, token, exat):
        self.redis.set(f'USER:{user_id}', jti, exat=exat)
        self.redis.set(jti, token, exat=exat)

    def get_existed_rtoken(self, user_id: int):
        jti = self.redis.get(f'USER:{user_id}')
        return self.redis.get(jti) if jti else None
