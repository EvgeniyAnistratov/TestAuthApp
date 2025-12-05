from .utils import read_variable
from .enums import ConfigVarType

_JWT_ACCESS_TTL_MINUTES = read_variable('JWT_ACCESS_TTL', ConfigVarType.INT, default=30, required=False)
JWT_ACCESS_TTL = 60 * _JWT_ACCESS_TTL_MINUTES

_JWT_ACCESS_TTL_HOURS = read_variable('JWT_REFRESH_TTL', ConfigVarType.INT, default=48, required=False)
JWT_REFRESH_TTL = 60 * 60 * _JWT_ACCESS_TTL_HOURS

JWT_SECRET_KEY = read_variable('JWT_SECRET_KEY', ConfigVarType.STR)