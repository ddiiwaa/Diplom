from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import allure

@pytest.fixture 
def driver():
    browser = webdriver.Chrome() 
    browser.maximize_window() 
    browser.implicitly_wait(4) 
    yield browser 
    browser.quit()

@allure.title("Просмотр фильма")
@allure.description("Только для авторизированных пользователей")   
@allure.severity("critical")
def test_auth_restriction(driver):
    """
 Метод получает сообщение об авторизации
 для доступа к просмотру фильма.
    """
    with allure.step("запустить браузер"):
        driver.get("https://www.kinopoisk.ru/?utm_referrer=trinixy.ru")
    driver.find_element(By.NAME, "kp_query").send_keys("Брат")
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.find_element(By.CSS_SELECTOR,'[href="/film/41519/sr/1/"]').click()
    driver.find_element(By.CSS_SELECTOR,'[data-test-id="Offer"]').click()

    with allure.step("проверка на запрос авторизации"):
        assert "Войдите или зарегистрируйтесь" in driver.find_element(By.CSS_SELECTOR, '.WelcomePage-tagline').text

@allure.title("Просмотр фильма")
@allure.description("Просмотр информации по конкретному фильму")   
@allure.severity("critical")
def test_check_information(driver):
    """
 Метод получает информацию о конкретном фильме
 по поиску.
    """
    driver.get("https://www.kinopoisk.ru/?utm_referrer=trinixy.ru")
    with allure.step("передать значение в поисковую строку"):
        driver.find_element(By.NAME, "kp_query").send_keys("Брат")
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.find_element(By.CSS_SELECTOR,'[href="/film/41519/sr/1/"]').click()

    with allure.step("проверка получения информации о фильме"):
        assert "Брат" in driver.find_element(By.CSS_SELECTOR, '.search_results_topText').text

@allure.title("Поиск фильма")
@allure.description("Поиск фильма по названию")   
@allure.severity("critical")
def test_check_information(driver):
    """
 Метод находит фильм по названию на кириллице.
    """
    driver.get("https://www.kinopoisk.ru/?utm_referrer=trinixy.ru")
    driver.find_element(By.NAME, "kp_query").send_keys("Брат")
    with allure.step("произвести поиск фильма"):
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    with allure.step("проверка результата поиска"):
        assert "Брат" in driver.find_element(By.CSS_SELECTOR, '.search_results_topText').text

@allure.title("Поиск фильма")
@allure.description("Поиск фильма по названию на латинице")   
@allure.severity("critical")
def test_check_information(driver):
    """
 Метод нахоит фильм по названию на латинице.
    """
    driver.get("https://www.kinopoisk.ru/?utm_referrer=trinixy.ru")
    driver.find_element(By.NAME, "kp_query").send_keys("Brat")
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    with allure.step("проверка результата поиска"):
        assert "Brat" in driver.find_element(By.CSS_SELECTOR, '.search_results_topText').text

@allure.title("Поиск фильма")
@allure.description("Поиск фильма по пустому значению")   
@allure.severity("critical")
def test_check_information(driver):
    """
 Метод выводит результат поиска фильма по пустому значению.
    """
    driver.get("https://www.kinopoisk.ru/?utm_referrer=trinixy.ru")
    driver.find_element(By.NAME, "kp_query").send_keys("")
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    with allure.step("проверка результата поиска"):
        assert driver.find_element(By.CSS_SELECTOR, '#search')
