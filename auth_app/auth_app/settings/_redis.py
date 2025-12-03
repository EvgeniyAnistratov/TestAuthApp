from .enums import ConfigVarType
from .utils import read_variable


REDIS_HOST = read_variable('REDIS_HOST', ConfigVarType.STR, default='redis', required=False)
REDIS_PORT = read_variable('REDIS_PORT', ConfigVarType.INT, default=6379, required=False)
