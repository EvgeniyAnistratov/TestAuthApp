from dotenv import load_dotenv
from django.core.exceptions import ImproperlyConfigured
from envparse import env

from .enums import ModeEnum, ConfigVarType


load_dotenv()


APP_MODE: ConfigVarType = env.str('APP_MODE', default=ModeEnum.DEV.value)
if APP_MODE not in ModeEnum.list():
    raise ImproperlyConfigured(
        f'Environment variable "APP_MODE" contains unsupported value "{APP_MODE}". List of supported values: '
        f'{ModeEnum.list()}.'
    )


if APP_MODE == ModeEnum.DEV.value:
    from .dev import *
elif APP_MODE == ModeEnum.PROD.value:
    from .prod import *