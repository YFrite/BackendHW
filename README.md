# FEFU HOMEWORKS PROJECT

## Pre-requirements
- Python 3.12

## Usage
- Build project

```make build```

- Run server in local network (LINUX ONLY / MACOS NOT CHECKED)

```make run-specific```

- Run in cloud

```make run```

## Description

### Task 1

Базовый сервер, приложение, настройки и т.д. присутствуют во всем проекте.
Запуск сервера в локальной сети осуществляется через ```python manage.py runserver $(IP_ADDR):8000```,
где IP_ADDR соответствует локальному айпи машины для доступа на других устройствах внутри сети.

### Task 2

В проекте содержится >= 2 GET и POST эндпоинтов.

Все эндпоинты:
1. /api/get_and_post [2 вида запросов привязаны к одному роуту, при пост запросе происходит редирект на второй эндпоинт]
2. /api/redirected [Эндпоинт для редиректа из первого пункта]
3. /api/users [GET, возвращает список пользователей]
4. /api/users/add [POST, тело в формате JSON{"name": your_name: str, "age": age: int}]
5. /api/users/update/:user_id [POST, тело в формате JSON{"name": your_name: Optional[str], "age": age: Optional[int]}]
6. /api/users/delete/:user_id [GET(по хорошему нужно пост, но не важно), удаляет пользователя с айди pk]

### Task 3

См. первые два эндпоинта

### Task 4

TODO

### Task 5

См. эндпоинты 3 - 6

### Task 6

TODO

### Task 7

Skipped

### Task 8

Ссылку отправил в лс
