import pytest


POSTS_ENDPOINT = "https://jsonplaceholder.typicode.com/posts"
POST_KEYS = ("userId", "id", "title", "body")


class TestPosts:
    """
    Тесты CRUD-операций на эндпойнте /posts публичного API JSONPlaceholder.
    """

    def test_get_all_posts(self, session):
        """Проверка получения списка всех постов."""
        response = session.get(POSTS_ENDPOINT)
        assert response.status_code == 200, "Статус-код должен быть 200"
        data = response.json()
        assert isinstance(data, list), "Ответ должен быть списком"
        assert len(data) > 0, "Список не должен быть пустым"
        # Проверка структуры первого объекта
        post = data[0]
        for key in POST_KEYS:
            assert key in post, f"Ключ '{key}' должен присутствовать в объекте"

    @pytest.mark.parametrize("post_id", [1, 50, 100])
    def test_get_single_post(self, session, post_id):
        """Проверка получения конкретного поста."""
        response = session.get(f"{POSTS_ENDPOINT}/{post_id}")

        assert response.status_code == 200, "Статус-код должен быть 200"
        data = response.json()

        assert isinstance(data, dict), "Ответ должен быть объектом"
        assert data["id"] == post_id, (
                              "ID в ответе должен совпадать с запрошенным"
                              )
        for key in POST_KEYS:
            assert key in data, f"Ключ '{key}' должен быть в JSON"

    @pytest.mark.parametrize(
        "payload",
        [
            {"title": "foo", "body": "bar", "userId": 1},
            {"title": "test", "body": "content", "userId": 5},
        ]
    )
    def test_create_post(self, session, payload):
        """Проверка создания поста."""
        response = session.post(POSTS_ENDPOINT, json=payload)

        assert response.status_code == 201, "POST должен возвращать 201"
        data = response.json()
        assert "id" in data, "Ответ должен содержать 'id'"
        for key in payload:
            assert data[key] == payload[key], f"Поле '{key}' должно совпадать"

    def test_update_post(self, session):
        """Проверка обновления поста через PUT."""
        post_id = 1
        payload = {
            "id": post_id,
            "title": "updated title",
            "body": "updated body",
            "userId": 1
        }
        response = session.put(f"{POSTS_ENDPOINT}/{post_id}", json=payload)
        assert response.status_code == 200, "PUT должен возвращать 200"
        data = response.json()
        assert data == payload, (
                        "Ответ должен соответствовать отправленным данным")

    def test_delete_post(self, session):
        """Проверка удаления поста."""
        post_id = 1
        response = session.delete(f"{POSTS_ENDPOINT}/{post_id}")
        assert response.status_code in (200, 204), (
            "DELETE должен вернуть 200 или 204")

    def test_get_nonexistent_post(self, session):
        """Негативный тест: запрос несуществующего поста."""
        response = session.get(f"{POSTS_ENDPOINT}/999999")
        assert response.status_code == 404, (
            "Для несуществующего поста должен быть 404")
        assert response.json() == {}, "Ответ должен быть пустым объектом"

    def test_put_invalid_post(self, session):
        """Негативный тест: обновление несуществующего поста."""
        payload = {
            "id": 0,
            "title": "x",
            "body": "y",
            "userId": 1
        }
        response = session.put(f"{POSTS_ENDPOINT}/0", json=payload)
        assert response.status_code in (404, 500), (
            "PUT должен возвращать 404 или 500 для несуществующего поста"
        )
