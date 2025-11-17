# Тестовое задание: Проверка CRUD операций /posts на JSONPlaceholder

## Описание проекта
Проект содержит тесты на Python с использованием `pytest` и `requests` для проверки базовых операций REST API 
(`GET`, `POST`, `PUT`, `DELETE`) на эндпойнте `/posts` публичного API JSONPlaceholder.  
Тесты проверяют статус-коды, структуру JSON-ответа, корректность данных и включают негативные сценарии.

## Установка зависимостей и запуск тестов
Установите необходимые библиотеки с помощью pip:
pip install -r requirements.txt
Для запуска всех тестов выполните:
pytest tests/ -v

## Структура проекта соответствует стнадартам Pytest
Тесты находятся в директории tests/.
Используется файл conftest.py для определения фикстур и общих настроек.


## Пример ожидаемого вывода тестов
tests/test_posts.py::TestPosts::test_get_all_posts PASSED
tests/test_posts.py::TestPosts::test_get_single_post[1] PASSED
tests/test_posts.py::TestPosts::test_get_single_post[50] PASSED
tests/test_posts.py::TestPosts::test_get_single_post[100] PASSED
tests/test_posts.py::TestPosts::test_create_post[{'title': 'foo', ...}] PASSED
tests/test_posts.py::TestPosts::test_create_post[{'title': 'test', ...}] PASSED
tests/test_posts.py::TestPosts::test_update_post PASSED
tests/test_posts.py::TestPosts::test_delete_post PASSED
tests/test_posts.py::TestPosts::test_get_nonexistent_post PASSED
tests/test_posts.py::TestPosts::test_put_invalid_post PASSED
