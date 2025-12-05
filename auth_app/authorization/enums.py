from enum import StrEnum


class ElementEnum(StrEnum):
    ARTICLE = 'ARTICLE'
    COMMENTS = 'COMMENTS'
    POSTS = 'POSTS'
    PROFILE = 'PROFILE'
    USER = 'USER'


class RoleEnum(StrEnum):
    ADMIN = 'ADMIN'
    EDITOR = 'EDITOR'
    GUEST = 'GUEST'
    MODERATOR = 'MODERATOR'
    USER = 'USER'

    @classmethod
    def list(cls) -> list[str]:
        return [i.value for i in RoleEnum]
