from django.core.exceptions import ImproperlyConfigured as DjangoImproperlyConfigured

from python_utils.settings import ConfigVarType, ImproperlyConfigured
from python_utils.settings import read_variable as _read_variable


def read_variable(
    name, v_type: ConfigVarType = ConfigVarType.STR, default: str | int | list[str] = None, required: bool = True
) -> str | int | list[str] | bool:
    """Overrides the python_utils.settings.read_variable.ImproperlyConfigured exception"""
    try:
        value = _read_variable(name, v_type, default, required)
    except ImproperlyConfigured as e:
        raise DjangoImproperlyConfigured(e)
    return value
