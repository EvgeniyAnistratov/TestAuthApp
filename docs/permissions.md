# Разграничение прав доступа
## Список ролей
- [ADMIN](#admin) - роль администратора
- [EDITOR](#editor) - роль редактора
- [GUEST](#guest) - роль гостя
- [MODERATOR](#moderator) - роль модератора
- [USER](#user) - роль пользователя

## Список прав доступа
- READ - чтение своих объектов
- READ_ALL - чтение всех объектов
- CREATE - создание объекта
- UPDATE - обновление своих объектов
- UPDATE_ALL - обновление всех объектов
- DELETE - удаление своих объектов
- DELETE_ALL - удаление всех объектов

## ADMIN
| Permission \ Element | ARTICLE | COMMENTS | POSTS | PROFILE | USER |
|:---------------------|:-------:|:--------:|:-----:|:-------:|:----:|
| READ                 | +       | +        | +     | +       | +    |
| READ_ALL             | +       | +        | +     | +       | +    |
| CREATE               | +       | +        | +     | +       | +    |
| UPDATE               | +       | +        | +     | +       | +    |
| UPDATE_ALL           | +       | +        | +     | +       | +    |
| DELETE               | +       | +        | +     | +       | +    |
| DELETE_ALL           | +       | +        | +     | +       | +    |

## EDITOR
| Permission \ Element | ARTICLE | COMMENTS | POSTS | PROFILE | USER |
|:---------------------|:-------:|:--------:|:-----:|:-------:|:----:|
| READ                 | +       | +        | +     | +       | +    |
| READ_ALL             | +       | +        | +     | +       | -    |
| CREATE               | -       | -        | -     | -       | -    |
| UPDATE               | -       | -        | -     | -       | -    |
| UPDATE_ALL           | +       | -        | -     | -       | -    |
| DELETE               | -       | -        | -     | -       | -    |
| DELETE_ALL           | -       | -        | -     | -       | -    |

## GUEST
| Permission \ Element | ARTICLE | COMMENTS | POSTS | PROFILE | USER |
|:---------------------|:-------:|:--------:|:-----:|:-------:|:----:|
| READ                 | +       | +        | +     | -       | -    |
| READ_ALL             | +       | +        | +     | -       | -    |
| CREATE               | -       | -        | -     | -       | -    |
| UPDATE               | -       | -        | -     | -       | -    |
| UPDATE_ALL           | -       | -        | -     | -       | -    |
| DELETE               | -       | -        | -     | -       | -    |
| DELETE_ALL           | -       | -        | -     | -       | -    |

## MODERATOR
| Permission \ Element | ARTICLE | COMMENTS | POSTS | PROFILE | USER |
|:---------------------|:-------:|:--------:|:-----:|:-------:|:----:|
| READ                 | +       | +        | +     | +       | +    |
| READ_ALL             | +       | +        | +     | +       | -    |
| CREATE               | -       | -        | -     | -       | -    |
| UPDATE               | -       | -        | -     | -       | -    |
| UPDATE_ALL           | -       | -        | -     | -       | -    |
| DELETE               | -       | -        | -     | -       | -    |
| DELETE_ALL           | -       | +        | +     | -       | -    |

## USER
| Permission \ Element | ARTICLE | COMMENTS | POSTS | PROFILE | USER |
|:---------------------|:-------:|:--------:|:-----:|:-------:|:----:|
| READ                 | +       | +        | +     | +       | +    |
| READ_ALL             | +       | +        | +     | +       | -    |
| CREATE               | +       | +        | +     | +       | -    |
| UPDATE               | +       | +        | +     | +       | +    |
| UPDATE_ALL           | -       | -        | -     | -       | -    |
| DELETE               | +       | +        | +     | +       | +    |
| DELETE_ALL           | -       | -        | -     | -       | -    |