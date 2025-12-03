# Описание переменных окружения
- [Описание переменных окружения](#описание-переменных-окружения)
  - [APP\_MODE](#app_mode)
  - [DB\_HOST](#db_host)
  - [DB\_NAME](#db_name)
  - [DB\_PASSWORD](#db_password)
  - [DB\_PORT](#db_port)
  - [DB\_USER](#db_user)
  - [DJ\_ALLOWED\_HOSTS](#dj_allowed_hosts)
  - [DJ\_DEBUG](#dj_debug)
  - [DJ\_SECRET\_KEY](#dj_secret_key)
  - [JWT\_ACCESS\_TTL](#jwt_access_ttl)
  - [JWT\_REFRESH\_TTL](#jwt_refresh_ttl)
  - [JWT\_SECRET\_KEY](#jwt_secret_key)
  - [REDIS\_HOST](#redis_host)
  - [REDIS\_PORT](#redis_port)

## APP_MODE
По умолчанию: __PROD__ <br />
Режим работы сервиса. Допустимые значения: DEV, PROD

## DB_HOST
По умолчанию: __db__ <br />
Хост БД. Если приложение будет запускаться в docker контейнере, и БД тоже будет запущена в docker контейнере,
то значение хоста должно хранить имя сервиса БД, описанного в docker-compose файле.

## DB_NAME
По умолчанию: __test_auth_app_db__ <br />
Имя БД.

## DB_PASSWORD
По умолчанию: __<не определена>__ <br />
Пароль пользователя БД.

## DB_PORT
По умолчанию: __5432__ <br />
Порт БД.

## DB_USER
По умолчанию: __postgres__ <br />
Имя роли для подключения к БД.

## DJ_ALLOWED_HOSTS
По умолчанию: __127.0.0.1,localhost__ <br />
Список хостов, которые будет обслуживать сервис. Хосты перечисляются через запятую без пробелов, например:
127.0.0.1, 198.55.22.1

## DJ_DEBUG
По умолчанию: __False__ <br />
Режим отладки. Допустимые значения: True, False

## DJ_SECRET_KEY
По умолчанию: __<не определена>__ <br />
Секретный ключ для Django, используемый для криптографической подписи.

## JWT_ACCESS_TTL
По умолчанию: __5__ <br />
Время жизни access токена в минутах.

## JWT_REFRESH_TTL
По умолчанию: __48__ <br />
Время жизни refresh токена в часах.

## JWT_SECRET_KEY
По умолчанию: __<не определена>__ <br />
Секретный ключ для jwt библиотеки.

## REDIS_HOST
По умолчанию: __redis__
Хост, на котором работает Redis. Если приложение будет запускаться в docker контейнере,
и Redis тоже будет запущен в docker контейнере, то значение хоста должно хранить имя сервиса Redis,
описанного в docker-compose файле.

## REDIS_PORT
По умолчанию: __6379__
Порт, на котором работает Redis.
