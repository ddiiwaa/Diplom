
import requests
import allure

Base_URL = "https://api.kinopoisk.dev/v1.4"

@allure.title("Поиск фильма")
@allure.description("Поиск фильма по ID")   
@allure.severity("critical")
def test_search():
    """
 Метод нахоит фильм по ID 5304403.
    """
    with allure.step("передат ключ"):
        my_headers = {"X-API-KEY": 'ZWKQHXN-FZ645SB-PKAE82N-TPPN8Y8'}
    result = requests.get(Base_URL + '/movie?page=1&limit=1&id=5304403', headers = my_headers)
    with allure.step("проверка статус кода"):
        assert result.status_code == 200

@allure.title("Поиск фильма")
@allure.description("Поиск фильма по названию")   
@allure.severity("critical")
def test_search_name():
    """
 Метод находит фильм по названию 'Брат'.
    """
    my_headers = {"X-API-KEY": 'ZWKQHXN-FZ645SB-PKAE82N-TPPN8Y8'}
    with allure.step("отправить get запрос"):
        result = requests.get(Base_URL + '/movie/search?page=1&limit=1&query=Брат', headers = my_headers)
    assert result.status_code == 200

@allure.title("Поиск фильма")
@allure.description("Поиск фильма по жанру")   
@allure.severity("critical")
def test_seach_kriminal():
    """
 Метод нахоит фильм по жанру 'криминал'.
    """
    my_headers = {"X-API-KEY": 'ZWKQHXN-FZ645SB-PKAE82N-TPPN8Y8'}
    result = requests.get(Base_URL + '/movie?page=1&limit=1&year=2023&genres.name=криминал', headers = my_headers)
    assert result.status_code == 200

@allure.title("Поиск фильма")
@allure.description("Поиск фильма по рейтингу")   
@allure.severity("critical")
def test_seach_rating():
    """
 Метод нахоит фильм по рейтингу от 8 до 10.
    """
    my_headers = {"X-API-KEY": 'ZWKQHXN-FZ645SB-PKAE82N-TPPN8Y8'}
    result = requests.get(Base_URL + '/movie?page=1&limit=1&rating.imdb=8-10', headers = my_headers)
    assert result.status_code == 200

@allure.title("Поиск фильма")
@allure.description("Поиск фильма с возрастным ограничением")   
@allure.severity("critical")
def test_seach_age():
    """
 Метод нахоит фильм с возрастным ограничением 18+.
    """
    my_headers = {"X-API-KEY": 'ZWKQHXN-FZ645SB-PKAE82N-TPPN8Y8'}
    result = requests.get(Base_URL + '/movie?page=1&limit=1&ageRating=18', headers = my_headers)
    assert result.status_code == 200

