# Тестовые данные
- [Тестовые данные](#тестовые-данные)
  - [Роли](#роли)
  - [Элементы приложения](#элементы-приложения)
  - [Разрешения](#разрешения)
  - [Пользователи](#пользователи)
  - [Статьи](#статьи)
  - [Комментарии статей](#комментарии-статей)
  - [Посты](#посты)
  - [Комментарии постов](#комментарии-постов)


## Роли
|id   |name|
|-----|----|
|1    |ADMIN|
|2    |EDITOR|
|3    |GUEST|
|4    |MODERATOR|
|5    |USER|


## Элементы приложения
|id   |name|
|-----|----|
|1    |ARTICLE|
|2    |COMMENTS|
|3    |POSTS|
|4    |PROFILE|
|5    |USER|


## Разрешения
|id   |read_permission|read_all_permission|create_permission|update_permission|update_all_permission|delete_permission|delete_all_permission|element_id|role_id|
|-----|---------------|-------------------|-----------------|-----------------|---------------------|-----------------|---------------------|----------|-------|
|1    |t              |t                  |t                |t                |t                    |t                |t                    |1         |1      |
|2    |t              |t                  |t                |t                |t                    |t                |t                    |2         |1      |
|3    |t              |t                  |t                |t                |t                    |t                |t                    |3         |1      |
|4    |t              |t                  |t                |t                |t                    |t                |t                    |4         |1      |
|5    |t              |t                  |t                |t                |t                    |t                |t                    |5         |1      |
|6    |t              |t                  |f                |f                |t                    |f                |f                    |1         |2      |
|7    |t              |t                  |f                |f                |f                    |f                |f                    |2         |2      |
|8    |t              |t                  |f                |f                |f                    |f                |f                    |3         |2      |
|9    |t              |t                  |f                |f                |f                    |f                |f                    |4         |2      |
|10   |t              |f                  |f                |f                |f                    |f                |f                    |5         |2      |
|11   |t              |t                  |f                |f                |f                    |f                |f                    |1         |3      |
|12   |t              |t                  |f                |f                |f                    |f                |f                    |2         |3      |
|13   |t              |t                  |f                |f                |f                    |f                |f                    |3         |3      |
|14   |f              |f                  |f                |f                |f                    |f                |f                    |4         |3      |
|15   |f              |f                  |f                |f                |f                    |f                |f                    |5         |3      |
|16   |t              |t                  |f                |f                |f                    |f                |f                    |1         |4      |
|17   |t              |t                  |f                |f                |f                    |f                |t                    |2         |4      |
|18   |t              |t                  |f                |f                |f                    |f                |t                    |3         |4      |
|19   |t              |t                  |f                |f                |f                    |f                |f                    |4         |4      |
|20   |t              |f                  |f                |f                |f                    |f                |f                    |5         |4      |
|21   |t              |t                  |t                |t                |f                    |t                |f                    |1         |5      |
|22   |t              |t                  |t                |t                |f                    |t                |f                    |2         |5      |
|23   |t              |t                  |t                |t                |f                    |t                |f                    |3         |5      |
|24   |t              |t                  |t                |t                |f                    |t                |f                    |4         |5      |
|25   |t              |f                  |f                |t                |f                    |t                |f                    |5         |5      |


## Пользователи
Пароли всех пользователей - password

Названия ролей пользователя записаны в его first_name

|id   |password|last_login          |first_name                    |last_name|middle_name|email                         |is_active|
|-----|--------|--------------------|------------------------------|---------|-----------|------------------------------|---------|
|1    |$2b$12$hwRB8i9IaFHhqQ6Mz9n4KONhfv231fmZ1YG3m6dSeEsHM.g9/8E3C|                    |ADMIN                         |         |           |admin@test.com                |t        |
|2    |$2b$12$a/15B8fMHBNjKwoTnaIDrubzFwG0Ny7ELy9.vO5LZ1pMF/PRWeuke|                    |USER1                         |         |           |user1@test.com                |t        |
|3    |$2b$12$lICkcgK4pzNbQvttEG.1YOCUpJOhKJTuBFd4FBS.rXDEAYkIkUDLm|                    |USER2                         |         |           |user2@test.com                |t        |
|4    |$2b$12$2Bljnz8j0.XcMZ7DeuDVReL5li7FbcB9xxo2bG6b1w0wogaa0F5Oa|                    |EDITOR                        |         |           |editor@test.com               |t        |
|5    |$2b$12$x2trWATIMFPKZYRbi2/nJeZu3L/T43GKSlKfQ/2nULII0mjcUsw/i|                    |USER_EDITOR                   |         |           |user_editor@test.com          |t        |
|6    |$2b$12$c8r4ckQueLJjfwPbslaCbOQFerr3ytHrkF2ubhDr529GV7/3QN/FW|                    |MODERATOR                     |         |           |moderator@test.com            |t        |
|7    |$2b$12$JR3cqnpLxECdOui1xg/HQePsDmnMxtgJfV8xCgbtbFckFIr2BvUoS|                    |USER_MODERATOR                |         |           |user_moderator@test.com       |t        |
|8    |$2b$12$ebTamPJ/D18kaY9Cuh1Zwuxgep4TF7LwPc4oh/dbm8CpXGvi6whcu|                    |USER_MODERATOR_EDITOR         |         |           |user_moderator_editor@test.com|t        |
|9    |$2b$12$y/ZCZN9ozvQClvwBmGdMaeU/V5dAcnl7HC.OyKUxdF.tbnlyCpInu|                    |GUEST                         |         |           |guest@test.com                |t        |


## Статьи
|id   |created_at|edited_at           |header                        |text|owner_id|
|-----|----------|--------------------|------------------------------|----|--------|
|1    |2025-12-05 18:49:22.789909+00|2025-12-05 18:49:22.789934+00|user1_article1_header         |user1_article1_text|2       |
|2    |2025-12-05 18:49:22.78995+00|2025-12-05 18:49:22.789953+00|user1_article1_header         |user1_article1_text|2       |
|3    |2025-12-05 18:49:22.78996+00|2025-12-05 18:49:22.789962+00|user2_article1_header         |user2_article1_text|3       |
|4    |2025-12-05 18:49:22.789967+00|2025-12-05 18:49:22.78997+00|user2_article1_header         |user2_article1_text|3       |
|5    |2025-12-05 18:49:22.789974+00|2025-12-05 18:49:22.789976+00|user1_article1_header         |user1_article1_text|5       |


## Комментарии статей
|id   |created_at|edited_at           |comment                       |article_id|owner_id|
|-----|----------|--------------------|------------------------------|----------|--------|
|1    |2025-12-05 18:49:22.791756+00|2025-12-05 18:49:22.791763+00|user1_comment1                |1         |2       |
|2    |2025-12-05 18:49:22.791775+00|2025-12-05 18:49:22.791778+00|user2_comment1                |1         |3       |
|3    |2025-12-05 18:49:22.791784+00|2025-12-05 18:49:22.791787+00|user1_comment2                |1         |2       |
|4    |2025-12-05 18:49:22.791793+00|2025-12-05 18:49:22.791795+00|user_editor_comment1          |2         |5       |
|5    |2025-12-05 18:49:22.791801+00|2025-12-05 18:49:22.791803+00|user1_comment1                |2         |2       |
|6    |2025-12-05 18:49:22.791809+00|2025-12-05 18:49:22.791813+00|user_moderator_editor_comment2|2         |8       |
|7    |2025-12-05 18:49:22.791819+00|2025-12-05 18:49:22.791822+00|user1_comment1                |3         |2       |
|8    |2025-12-05 18:49:22.791827+00|2025-12-05 18:49:22.791829+00|user2_comment1                |3         |3       |
|9    |2025-12-05 18:49:22.791835+00|2025-12-05 18:49:22.791837+00|user1_comment2                |3         |2       |
|10   |2025-12-05 18:49:22.791842+00|2025-12-05 18:49:22.791845+00|user_editor_comment1          |4         |5       |
|11   |2025-12-05 18:49:22.79185+00|2025-12-05 18:49:22.791852+00|user1_comment1                |4         |2       |
|12   |2025-12-05 18:49:22.791858+00|2025-12-05 18:49:22.79186+00|user_moderator_editor_comment2|4         |8       |
|13   |2025-12-05 18:49:22.791865+00|2025-12-05 18:49:22.791868+00|user2_comment1                |5         |3       |


## Посты
|id   |created_at|edited_at           |header                        |text|owner_id|
|-----|----------|--------------------|------------------------------|----|--------|
|1    |2025-12-05 18:28:46.167981+00|2025-12-05 18:28:46.167988+00|user1_post1_header            |user1_post1_text|2       |
|2    |2025-12-05 18:28:46.167999+00|2025-12-05 18:28:46.168002+00|user1_post1_header            |user1_post1_text|2       |
|3    |2025-12-05 18:28:46.168007+00|2025-12-05 18:28:46.168009+00|user2_post1_header            |user2_post1_text|3       |
|4    |2025-12-05 18:28:46.168013+00|2025-12-05 18:28:46.168014+00|user2_post1_header            |user2_post1_text|3       |
|5    |2025-12-05 18:28:46.168018+00|2025-12-05 18:28:46.168019+00|user1_post1_header            |user1_post1_text|5       |


## Комментарии постов
|id   |created_at|edited_at           |comment                       |owner_id|post_id|
|-----|----------|--------------------|------------------------------|--------|-------|
|1    |2025-12-05 18:28:46.169038+00|2025-12-05 18:28:46.169043+00|user1_comment1                |2       |1      |
|2    |2025-12-05 18:28:46.169052+00|2025-12-05 18:28:46.169054+00|user2_comment1                |3       |1      |
|3    |2025-12-05 18:28:46.169059+00|2025-12-05 18:28:46.169061+00|user1_comment2                |2       |1      |
|4    |2025-12-05 18:28:46.169065+00|2025-12-05 18:28:46.169067+00|user_editor_comment1          |5       |2      |
|5    |2025-12-05 18:28:46.169071+00|2025-12-05 18:28:46.169072+00|user1_comment1                |2       |2      |
|6    |2025-12-05 18:28:46.169076+00|2025-12-05 18:28:46.169078+00|user_moderator_editor_comment2|8       |2      |
|7    |2025-12-05 18:28:46.169081+00|2025-12-05 18:28:46.169083+00|user1_comment1                |2       |3      |
|8    |2025-12-05 18:28:46.169086+00|2025-12-05 18:28:46.169088+00|user2_comment1                |3       |3      |
|9    |2025-12-05 18:28:46.169091+00|2025-12-05 18:28:46.169093+00|user1_comment2                |2       |3      |
|10   |2025-12-05 18:28:46.169097+00|2025-12-05 18:28:46.169099+00|user_editor_comment1          |5       |4      |
|11   |2025-12-05 18:28:46.169102+00|2025-12-05 18:28:46.169104+00|user1_comment1                |2       |4      |
|12   |2025-12-05 18:28:46.169108+00|2025-12-05 18:28:46.169109+00|user_moderator_editor_comment2|8       |4      |
|13   |2025-12-05 18:28:46.169113+00|2025-12-05 18:28:46.169115+00|user2_comment1                |3       |5      |

