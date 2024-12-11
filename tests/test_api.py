import pytest
import requests
import allure
from config.settings import API_URL, TOKEN
from config.test_data import MOVIE_ID

@allure.feature('API Tests')
class TestAPI:

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Get movie information')
    def test_get_movie_info(self):
        response = requests.get(f"{API_URL}/movies/{MOVIE_ID}", headers={"X-API-KEY": TOKEN})
        assert response.status_code == 200
        data = response.json()
        assert 'name' in data  # Предполагается, что поле 'name' должно существовать

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Search movie by title')
    def test_search_movie(self):
        params = {"keyword": "Тест"} 
        response = requests.get(f"{API_URL}/movies/search", headers={"X-API-KEY": TOKEN}, params=params)
        assert response.status_code == 200
        data = response.json()
        assert len(data['movies']) > 0  # Проверяем, что есть фильмы в результатах

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Get movie ratings')
    def test_get_movie_ratings(self):
        response = requests.get(f"{API_URL}/movies/{MOVIE_ID}/ratings", headers={"X-API-KEY": TOKEN})
        assert response.status_code == 200
        data = response.json()
        assert 'rating' in data  # Проверяем наличие рейтинга

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Check if a movie exists')
    def test_check_movie_exists(self):
        response = requests.get(f"{API_URL}/movies/{MOVIE_ID}", headers={"X-API-KEY": TOKEN})
        assert response.status_code == 200
        data = response.json()
        assert data['id'] == MOVIE_ID  # Проверяем, что ID совпадает

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Handle movie not found error')
    def test_movie_not_found(self):
        response = requests.get(f"{API_URL}/movies/9999999", headers={"X-API-KEY": TOKEN})
        assert response.status_code == 404  # Проверяем, что получаем ошибку 404