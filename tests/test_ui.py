import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from config.settings import BASE_URL, TOKEN
from config.test_data import MOVIE_ID, SEARCH_TERM

@allure.feature('UI Tests')
class TestUI:

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Opening the main page')
    def test_open_main_page(self):
        driver = webdriver.Firefox()  # Используем Firefox
        driver.get(BASE_URL)
        assert "КиноПоиск" in driver.title
        driver.quit()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Search for a movie')
    def test_search_movie(self):
        driver = webdriver.Firefox()
        driver.get(BASE_URL)
        search_box = driver.find_element(By.NAME, "text")
        search_box.send_keys(SEARCH_TERM)
        search_box.submit()
        assert SEARCH_TERM in driver.title
        driver.quit()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Check movie details page')
    def test_movie_details(self):
        driver = webdriver.Firefox()
        driver.get(f"{BASE_URL}/film/{MOVIE_ID}/")  # Используем реальный ID
        assert "КиноПоиск" in driver.page_source  # Проверка наличия контента
        driver.quit()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Check user login functionality')
    def test_login_functionality(self):
        driver = webdriver.Firefox()
        driver.get(BASE_URL)
        # Установка куки для токена авторизации
        driver.add_cookie({"name": "auth_token", "value": TOKEN})
        driver.refresh()
        assert "Войти" not in driver.page_source  # Проверка, что кнопка "Войти" отсутствует
        driver.quit()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Check footer links')
    def test_footer_links(self):
        driver = webdriver.Firefox()
        driver.get(BASE_URL)
        footer_links = driver.find_elements(By.CSS_SELECTOR, "footer a")
        assert len(footer_links) > 0  # Проверяем, что подвал содержит ссылки
        driver.quit()