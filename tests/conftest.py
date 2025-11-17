import pytest
import requests


@pytest.fixture(scope="class")
def session():
    """
    Фикстура создаёт HTTP-сессию перед запуском тестов класса
    и закрывает её после выполнения тестов.
    """
    s = requests.Session()
    yield s
    s.close()
