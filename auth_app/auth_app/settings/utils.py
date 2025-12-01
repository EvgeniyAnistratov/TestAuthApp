from django.core.exceptions import ImproperlyConfigured
from envparse import env, ConfigurationError

from .enums import ConfigVarType


def read_variable(
    name, v_type: ConfigVarType = ConfigVarType.STR, default: str | int | list[str] = None, required: bool = True
) -> str | int | list[str] | bool:
    if v_type == ConfigVarType.STR:
        value = env.str(name, default=default)
    elif v_type == ConfigVarType.LIST_STR:
        value = env(name, cast=list, subcast=str, default=default)
    elif v_type == ConfigVarType.BOOL:
        value = env.bool(name, default=default)
    elif v_type == ConfigVarType.INT:
        try:
            value = env.int(name, default=default)
        except ConfigurationError as e:
            if 'invalid literal for int()' in str(e):
                raise ImproperlyConfigured(f'Environment variable "{name}" is wrong.')
            else:
                raise e
    else:
        raise ImproperlyConfigured(f'Unknown v_type "{v_type}" while reading {name} variable.')
    if (value is None or value == '') and required:
        raise ImproperlyConfigured(f'Environment variable "{name}" is required.')
    return value
