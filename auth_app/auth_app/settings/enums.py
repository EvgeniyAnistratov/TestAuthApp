from enum import Enum


class ModeEnum(Enum):
    DEV = 'DEV'
    PROD = 'PROD'

    @classmethod
    def list(cls) -> list[str]:
        return [i.value for i in ModeEnum]
