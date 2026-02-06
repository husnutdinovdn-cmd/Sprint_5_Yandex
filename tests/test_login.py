"""
Тесты для входа в аккаунт Stellar Burgers
Проверяет 4 способа входа в систему
"""
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.forgot_password_page import ForgotPasswordPage


class TestLogin:
    """Класс тестов для входа в аккаунт"""
    
    def test_login_via_main_page_button(self, browser, registered_user):
        """
        Тест входа через кнопку "Войти в аккаунт" на главной странице
        """
        # Открываем главную страницу
        main_page = MainPage(browser)
        main_page.open()
        
        # Кликаем на кнопку "Войти в аккаунт"
        main_page.click_login_button()
        login_page = LoginPage(browser)
        login_page.wait_for_page_load()
        
        # Выполняем вход
        login_page.login(registered_user['email'], registered_user['password'])
        
        # Проверяем, что произошел переход на главную страницу
        main_page.wait_for_page_load()
        main_page.wait_for_url_contains("stellarburgers.nomoreparties.site")
        assert "stellarburgers.nomoreparties.site" in main_page.get_current_url(), \
            "После входа должен произойти переход на главную страницу"
    
    def test_login_via_personal_account_button(self, browser, registered_user):
        """
        Тест входа через кнопку "Личный кабинет" на главной странице
        """
        # Открываем главную страницу
        main_page = MainPage(browser)
        main_page.open()
        
        # Кликаем на кнопку "Личный кабинет"
        main_page.click_personal_account_button()
        login_page = LoginPage(browser)
        login_page.wait_for_page_load()
        
        # Выполняем вход
        login_page.login(registered_user['email'], registered_user['password'])
        
        # Проверяем, что произошел переход на главную страницу
        main_page.wait_for_page_load()
        main_page.wait_for_url_contains("stellarburgers.nomoreparties.site")
        assert "stellarburgers.nomoreparties.site" in main_page.get_current_url(), \
            "После входа должен произойти переход на главную страницу"
    
    def test_login_via_registration_page_button(self, browser, registered_user):
        """
        Тест входа через кнопку "Войти" на странице регистрации
        """
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
        
        # Кликаем на кнопку "Войти"
        registration_page.click_login_link()
        login_page.wait_for_page_load()
        
        # Выполняем вход
        login_page.login(registered_user['email'], registered_user['password'])
        
        # Проверяем, что произошел переход на главную страницу
        main_page.wait_for_page_load()
        main_page.wait_for_url_contains("stellarburgers.nomoreparties.site")
        assert "stellarburgers.nomoreparties.site" in main_page.get_current_url(), \
            "После входа должен произойти переход на главную страницу"
    
    def test_login_via_forgot_password_page_button(self, browser, registered_user):
        """
        Тест входа через кнопку "Войти" на странице восстановления пароля
        """
        # Открываем главную страницу
        main_page = MainPage(browser)
        main_page.open()
        
        # Переходим на страницу входа
        main_page.click_login_button()
        login_page = LoginPage(browser)
        login_page.wait_for_page_load()
        
        # Переходим на страницу восстановления пароля
        login_page.click_forgot_password_link()
        forgot_password_page = ForgotPasswordPage(browser)
        forgot_password_page.wait_for_page_load()
        
        # Кликаем на кнопку "Войти"
        forgot_password_page.click_login_link()
        login_page.wait_for_page_load()
        
        # Выполняем вход
        login_page.login(registered_user['email'], registered_user['password'])
        
        # Проверяем, что произошел переход на главную страницу
        main_page.wait_for_page_load()
        main_page.wait_for_url_contains("stellarburgers.nomoreparties.site")
        assert "stellarburgers.nomoreparties.site" in main_page.get_current_url(), \
            "После входа должен произойти переход на главную страницу"
