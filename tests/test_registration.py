"""
Тесты для регистрации пользователя в Stellar Burgers
"""
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from utils.data_generator import generate_test_data, generate_invalid_password


class TestRegistration:
    """Класс тестов для регистрации"""
    
    def test_successful_registration(self, browser, generate_test_data_fixture):
        """
        Тест успешной регистрации пользователя
        Проверяет, что пользователь может зарегистрироваться с валидными данными
        """
        # Генерируем тестовые данные
        test_data = generate_test_data_fixture
        
        # Открываем главную страницу
        main_page = MainPage(browser)
        main_page.open()
        
        # Переходим на страницу входа
        main_page.click_login_button()
        login_page = LoginPage(browser)
        login_page.wait_for_page_load()
        
        # Переходим на страницу регистрации
        login_page.click_register_link()
        registration_page = RegistrationPage(browser)
        registration_page.wait_for_page_load()
        
        # Выполняем регистрацию
        registration_page.register(
            test_data['name'],
            test_data['email'],
            test_data['password']
        )
        
        # Проверяем, что после регистрации произошел переход на страницу входа
        login_page.wait_for_page_load()
        login_page.wait_for_url_contains("login")
        assert login_page.get_current_url() == "https://stellarburgers.nomoreparties.site/login", \
            "После регистрации должен произойти переход на страницу входа"
    
    def test_registration_with_invalid_password(self, browser):
        """
        Тест регистрации с некорректным паролем (<6 символов)
        Проверяет, что отображается ошибка для пароля менее 6 символов
        """
        # Генерируем тестовые данные с невалидным паролем
        test_data = generate_test_data()
        invalid_password = generate_invalid_password()
        
        # Открываем главную страницу
        main_page = MainPage(browser)
        main_page.open()
        
        # Переходим на страницу входа
        main_page.click_login_button()
        login_page = LoginPage(browser)
        login_page.wait_for_page_load()
        
        # Переходим на страницу регистрации
        login_page.click_register_link()
        registration_page = RegistrationPage(browser)
        registration_page.wait_for_page_load()
        
        # Пытаемся зарегистрироваться с невалидным паролем
        registration_page.register(
            test_data['name'],
            test_data['email'],
            invalid_password
        )
        
        # Проверяем, что отображается ошибка
        assert registration_page.is_password_error_displayed(), \
            "Должна отображаться ошибка для пароля менее 6 символов"
