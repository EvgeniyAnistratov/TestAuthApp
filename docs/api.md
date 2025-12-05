# Описание API
- [Описание API](#описание-api)
  - [/auth/ - API регистрации и аутентификации](#auth---api-регистрации-и-аутентификации)
    - [POST /auth/register](#post-authregister)
    - [POST /auth/login](#post-authlogin)
    - [POST /auth/logout](#post-authlogout)
    - [POST /auth/refresh](#post-authrefresh)
  - [/users/ - API работы с пользователями](#users---api-работы-с-пользователями)
    - [GET /users/id](#get-usersid)
    - [DELETE /users/id](#delete-usersid)
    - [PATCH /users/id](#patch-usersid)
    - [POST /users/id/add-roles](#post-usersidadd-roles)
    - [POST /users/id/delete-roles](#post-usersiddelete-roles)
  - [/authorization/ - API редактирования прав доступа](#authorization---api-редактирования-прав-доступа)
    - [GET /authorization/elements](#get-authorizationelements)
    - [GET /authorization/permissions](#get-authorizationpermissions)
    - [GET /authorization/permissions/id](#get-authorizationpermissionsid)
    - [PATCH /authorization/permissions/id](#patch-authorizationpermissionsid)
    - [GET /authorization/roles](#get-authorizationroles)
  - [/posts/ - API работы с постами](#posts---api-работы-с-постами)
    - [GET /posts](#get-posts)
    - [POST /posts](#post-posts)
    - [GET /posts/id](#get-postsid)
    - [PATCH /posts/id](#patch-postsid)
    - [GET /posts/id/comments](#get-postsidcomments)
    - [POST /posts/comments](#post-postscomments)
    - [GET /posts/comments/id](#get-postscommentsid)
    - [DELETE /posts/comments/id](#delete-postscommentsid)
    - [PATCH /posts/comments/id](#patch-postscommentsid)
  - [/articles/ - API работы со статьями](#articles---api-работы-со-статьями)
    - [GET /articles](#get-articles)
    - [POST /articles](#post-articles)
    - [GET /articles/id](#get-articlesid)
    - [PATCH /articles/id](#patch-articlesid)
    - [GET /articles/id/comments](#get-articlesidcomments)
    - [POST /articles/comments](#post-articlescomments)
    - [GET /articles/comments/id](#get-articlescommentsid)
    - [DELETE /articles/comments/id](#delete-articlescommentsid)
    - [PATCH /articles/comments/id](#patch-articlescommentsid)

## /auth/ - API регистрации и аутентификации
### POST /auth/register
Регистрация нового пользователя.

Тело запроса
```json
{
    "first_name": "Name",
    "last_name": "Last name",
    "middle_name": "Middle name",
    "email": "address@test.com",
    "password": "strong_secret_password",
    "repeat_password": "strong_secret_password"
}
```

<details>
<summary>Ответ</summary>

```json
{
    "id": 1,
    "first_name": "Name",
    "last_name": "Last name",
    "middle_name": "Middle name",
    "email": "address@test.com"
}
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"first_name":"user", "email": "user@test.com", "password": "password", "repeat_password": "password"}' \
     "http://127.0.0.1:8000/auth/register"
```
</details>
<hr>


### POST /auth/login
Вход в систему, получение JWT токенов

Тело запроса
```json
{
    "email": "address@test.com",
    "password": "strong_secret_password"
}
```

<details>
<summary>Ответ</summary>

```json
{
    "access_token": "ACCESS_TOKEN",
    "refresh_token": "REFRESH_TOKEN"
}
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"email": "user@test.com", "password": "password"}' \
     "http://127.0.0.1:8000/auth/login"
```
</details>
<hr>


### POST /auth/logout
Выход из системы

<details>
<summary>curl</summary>

```bash
curl -X POST \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     "http://127.0.0.1:8000/auth/logout"
```
</details>
<hr>


### POST /auth/refresh
 Получение нового ACCESS и REFRESH токенов.

Тело запроса
```json
{
    "refresh_token": "REFRESH_TOKEN"
}
```

<details>
<summary>Ответ</summary>

```json
{
    "access_token": "ACCESS_TOKEN",
    "refresh_token": "REFRESH_TOKEN"
}
```
</details>
<hr>

<details>
<summary>curl</summary>

```bash
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"refresh_token": "REFRESH_TOKEN"}' \
     "http://127.0.0.1:8000/auth/refresh"
```
</details>
<hr>


## /users/ - API работы с пользователями
### GET /users/id
Получение инфорации о пользователе

<details>
<summary>Ответ</summary>

```json
{
    "id": 1,
    "first_name": "Name",
    "last_name": "Last name",
    "middle_name": "Middle name",
    "email": "address@test.com"
}
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X GET \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     "http://127.0.0.1:8000/users/1"
```
</details>
<hr>


### DELETE /users/id
Удаление пользователя

<details>
<summary>curl</summary>

```bash
curl -X DELETE \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     "http://127.0.0.1:8000/users/1"
```
</details>
<hr>


### PATCH /users/id
Обновление инофрмации о пользователе

Тело запроса
```json
{
    "first_name": "NewName",
    "last_name": "NewLastName",
    "middle_name": "NewMiddleName",
    "email": "new_email@test.com"
}
```

<details>
<summary>curl</summary>

```bash
curl -X PATCH \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     -d '{"first_name":"new_name", "last_name": "new_last_name"}' \
     "http://127.0.0.1:8000/users/1"
```
</details>
<hr>


### POST /users/id/add-roles
Добавление ролей пользователю

Тело запроса
```json
{
    "roles": [2,3,4]
}
```

<details>
<summary>curl</summary>

```bash
curl -X POST \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     -d '{"roles": [2,3,4]}' \
     "http://127.0.0.1:8000/users/1/add-roles"
```
</details>
<hr>


### POST /users/id/delete-roles
Удаление ролей пользователя

Тело запроса
```json
{
    "roles": [2,3,4]
}
```

<details>
<summary>curl</summary>

```bash
curl -X POST \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     -d '{"roles": [2,3,4]}' \
     "http://127.0.0.1:8000/users/1/delete-roles"
```
</details>
<hr>


## /authorization/ - API редактирования прав доступа
### GET /authorization/elements
Получение списка элементов приложения

<details>
<summary>Ответ</summary>

```json
[
    {"id": 1, "name": "ARTICLE"},
    {"id": 2, "name": "COMMENTS"},
    {"id": 3, "name": "POSTS"},
    {"id": 4, "name": "PROFILE"},
    {"id": 5, "name": "USER"}
]
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X GET \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     "http://127.0.0.1:8000/authorization/elements"
```
</details>
<hr>


### GET /authorization/permissions
Получение списка разрешений. Может фильтровать разрешения по параметрам запроса: role_id, element_id

<details>
<summary>Ответ</summary>

```json
[
    {
        "id": 1,
        "read_permission": true,
        "read_all_permission": true,
        "create_permission": true,
        "update_permission": true,
        "update_all_permission": true,
        "delete_permission": true,
        "delete_all_permission": true,
        "element": 1,
        "role ":1
    }
]
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X GET \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     "http://127.0.0.1:8000/authorization/permissions?role_id=1&element_id=1"
```
</details>
<hr>


### GET /authorization/permissions/id
Получение разрешения по id

<details>
<summary>Ответ</summary>

```json
{
    "id": 1,
    "read_permission": true,
    "read_all_permission": true,
    "create_permission": true,
    "update_permission": true,
    "update_all_permission": true,
    "delete_permission": true,
    "delete_all_permission": true,
    "element": 1,
    "role ":1
}
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X GET \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     "http://127.0.0.1:8000/authorization/permissions/1"
```
</details>
<hr>


### PATCH /authorization/permissions/id
Получение разрешения по id

Тело запроса
```json
{
    "read_permission": true,
    "read_all_permission": true,
    "create_permission": true,
    "update_permission": true,
    "update_all_permission": true,
    "delete_permission": true,
    "delete_all_permission": true,
}
```

<details>
<summary>Ответ</summary>

```json
{
    "id": 1,
    "read_permission": true,
    "read_all_permission": true,
    "create_permission": true,
    "update_permission": true,
    "update_all_permission": true,
    "delete_permission": true,
    "delete_all_permission": true,
    "element": 1,
    "role ":1
}
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X PATCH \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     -d '{"read_permission": true, "read_all_permission": false}' \
     "http://127.0.0.1:8000/authorization/permissions/1"
```
</details>
<hr>


### GET /authorization/roles
Получение списка ролей

<details>
<summary>Ответ</summary>

```json
[
    {"id": 1, "name": "ADMIN"},
    {"id": 2, "name": "EDITOR"},
    {"id": 3, "name": "GUEST"},
    {"id": 4, "name": "MODERATOR"},
    {"id": 5, "name": "USER"}
]
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X GET \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     "http://127.0.0.1:8000/authorization/roles"
```
</details>
<hr>


## /posts/ - API работы с постами
### GET /posts
Получение списка всех постов

<details>
<summary>Ответ</summary>

```json
[
    {
        "id": 1,
        "header": "PostHeader",
        "text": "PostText",
        "owner": 1
    }
]
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X GET \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     "http://127.0.0.1:8000/posts"
```
</details>
<hr>


### POST /posts
Публикация поста

Тело запроса
```json
{
    "header": "PostHeader",
    "text": "PostText",
}
```

<details>
<summary>Ответ</summary>

```json
{
    "id": 1,
    "header": "PostHeader",
    "text": "PostText",
    "owner": 1
}
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X POST \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     -d '{"header": "PostHeader", "text": "PostText"}' \
     "http://127.0.0.1:8000/posts"
```
</details>
<hr>


### GET /posts/id
Получение поста по id

<details>
<summary>Ответ</summary>

```json
{
    "id": 1,
    "header": "PostHeader",
    "text": "PostText",
    "owner": 1
}
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X GET \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     "http://127.0.0.1:8000/posts/1"
```
</details>
<hr>


### PATCH /posts/id
Обновление поста

Тело запроса
```json
{
    "header": "UpdatedPostHeader",
    "text": "UpdatedPostText",
}
```

<details>
<summary>Ответ</summary>

```json
{
    "id": 1,
    "header": "UpdatedPostHeader",
    "text": "UpdatedPostText",
    "owner": 1
}
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X PATCH \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     -d '{"header": "UpdatedHeader", "text": "UpdatedText"}' \
     "http://127.0.0.1:8000/posts/1"
```
</details>
<hr>


### GET /posts/id/comments
Получение комментариев поста

<details>
<summary>Ответ</summary>

```json
[
    {
        "id": 1,
        "created_at": "2025-12-05T12:09:07.037763Z",
        "edited_at": "2025-12-05T12:13:29.775792Z",
        "comment": "Comment",
        "owner": 1,
        "post": 1
    }
]
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X GET \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     "http://127.0.0.1:8000/posts/1/comments"
```
</details>
<hr>


### POST /posts/comments
Публикация комментария

Тело запроса
```json
{
    "post": 1,
    "comment": "New comment",
}
```

<details>
<summary>Ответ</summary>

```json
{
    "id": 1,
    "created_at": "2025-12-05T12:09:07.037763Z",
    "edited_at": "2025-12-05T12:13:29.775792Z",
    "comment": "New comment",
    "owner": 1,
    "post": 1
}
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X POST \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     -d '{"post": 1, "comment": "New comment"}' \
     "http://127.0.0.1:8000/posts/comments"
```
</details>
<hr>


### GET /posts/comments/id
Получение комментария по id

<details>
<summary>Ответ</summary>

```json
{
    "id": 1,
    "created_at": "2025-12-05T12:09:07.037763Z",
    "edited_at": "2025-12-05T12:13:29.775792Z",
    "comment": "Сomment",
    "owner": 1,
    "post": 1
}
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X GET \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     "http://127.0.0.1:8000/posts/comments/1"
```
</details>
<hr>


### DELETE /posts/comments/id
Удаление комментария по id

<details>
<summary>curl</summary>

```bash
curl -X DELETE \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     "http://127.0.0.1:8000/posts/comments/1"
```
</details>
<hr>


### PATCH /posts/comments/id
Редактирование комментария по id

Тело запроса
```json
{
    "comment": "Edited comment",
}
```

<details>
<summary>Ответ</summary>

```json
[
    {
        "id": 1,
        "created_at": "2025-12-05T12:09:07.037763Z",
        "edited_at": "2025-12-05T12:13:29.775792Z",
        "comment": "Edited comment",
        "owner": 1,
        "post": 1
    }
]
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X PATCH \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     -d '{"comment": "New comment"}' \
     "http://127.0.0.1:8000/posts/comments/1"
```
</details>
<hr>


## /articles/ - API работы со статьями
### GET /articles
Получение списка всех статей

<details>
<summary>Ответ</summary>

```json
[
    {
        "id": 1,
        "header": "ArticleHeader",
        "text": "ArticleText",
        "owner": 1
    }
]
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X GET \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     "http://127.0.0.1:8000/articles"
```
</details>
<hr>


### POST /articles
Публикация статьи

Тело запроса
```json
{
    "header": "ArticleHeader",
    "text": "ArticleText",
}
```

<details>
<summary>Ответ</summary>

```json
{
    "id": 1,
    "header": "ArticleHeader",
    "text": "ArticleText",
    "owner": 1
}
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X POST \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     -d '{"header": "ArticleHeader", "text": "ArticleText"}' \
     "http://127.0.0.1:8000/articles"
```
</details>
<hr>


### GET /articles/id
Получение статьи по id

<details>
<summary>Ответ</summary>

```json
{
    "id": 1,
    "header": "ArticleHeader",
    "text": "ArticleText",
    "owner": 1
}
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X GET \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     "http://127.0.0.1:8000/articles/1"
```
</details>
<hr>


### PATCH /articles/id
Обновление статьи

Тело запроса
```json
{
    "header": "UpdatedArticleHeader",
    "text": "UpdatedArticleText",
}
```

<details>
<summary>Ответ</summary>

```json
{
    "id": 1,
    "header": "UpdatedArticleHeader",
    "text": "UpdatedArticleText",
    "owner": 1
}
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X PATCH \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     -d '{"header": "UpdatedArticleHeader", "text": "UpdatedArticleText"}' \
     "http://127.0.0.1:8000/articles/1"
```
</details>
<hr>


### GET /articles/id/comments
Получение комментариев статьи

<details>
<summary>Ответ</summary>

```json
[
    {
        "id": 1,
        "created_at": "2025-12-05T12:09:07.037763Z",
        "edited_at": "2025-12-05T12:13:29.775792Z",
        "comment": "Comment",
        "owner": 1,
        "article": 1
    }
]
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X GET \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     "http://127.0.0.1:8000/articles/1/comments"
```
</details>
<hr>


### POST /articles/comments
Публикация комментария

Тело запроса
```json
{
    "article": 1,
    "comment": "New comment",
}
```

<details>
<summary>Ответ</summary>

```json
{
    "id": 1,
    "created_at": "2025-12-05T12:09:07.037763Z",
    "edited_at": "2025-12-05T12:13:29.775792Z",
    "comment": "New comment",
    "owner": 1,
    "article": 1
}
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X POST \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     -d '{"article": 1, "comment": "New comment"}' \
     "http://127.0.0.1:8000/articles/comments"
```
</details>
<hr>


### GET /articles/comments/id
Получение комментария по id

<details>
<summary>Ответ</summary>

```json
{
    "id": 1,
    "created_at": "2025-12-05T12:09:07.037763Z",
    "edited_at": "2025-12-05T12:13:29.775792Z",
    "comment": "Сomment",
    "owner": 1,
    "article": 1
}
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X GET \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     "http://127.0.0.1:8000/articles/comments/1"
```
</details>
<hr>


### DELETE /articles/comments/id
Удаление комментария по id

<details>
<summary>curl</summary>

```bash
curl -X DELETE \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     "http://127.0.0.1:8000/articles/comments/1"
```
</details>
<hr>


### PATCH /articles/comments/id
Редактирование комментария по id

Тело запроса
```json
{
    "comment": "Edited comment",
}
```

<details>
<summary>Ответ</summary>

```json
[
    {
        "id": 1,
        "created_at": "2025-12-05T12:09:07.037763Z",
        "edited_at": "2025-12-05T12:13:29.775792Z",
        "comment": "Edited comment",
        "owner": 1,
        "article": 1
    }
]
```
</details>

<details>
<summary>curl</summary>

```bash
curl -X PATCH \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer ACCESS_TOKEN" \
     -d '{"comment": "New comment"}' \
     "http://127.0.0.1:8000/articles/comments/1"
```
</details>
<hr>
