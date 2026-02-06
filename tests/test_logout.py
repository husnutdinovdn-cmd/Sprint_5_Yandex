"""
Тесты для выхода из аккаунта Stellar Burgers
"""
import pytest
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage


class TestLogout:
    """Класс тестов для выхода из аккаунта"""
    
    def test_logout_from_personal_account(self, browser, logged_in_user):
        """
        Тест выхода из аккаунта по кнопке "Выйти" в личном кабинете
        """
        # Открываем главную страницу (уже авторизованы)
        main_page = MainPage(browser)
        main_page.open()
        main_page.wait_for_page_load()
        
        # Переходим в личный кабинет
        main_page.click_personal_account_button()
        profile_page = ProfilePage(browser)
        profile_page.wait_for_page_load()
        
        # Выполняем выход
        profile_page.click_logout_button()
        
        # Проверяем, что произошел переход на страницу входа
        login_page = LoginPage(browser)
        login_page.wait_for_page_load()
        login_page.wait_for_url_contains("login")
        assert "login" in login_page.get_current_url().lower(), \
            "После выхода должен произойти переход на страницу входа"
        
        # Проверяем, что мы не можем попасть в личный кабинет без авторизации
        main_page.open()
        main_page.click_personal_account_button()
        login_page.wait_for_page_load()
        login_page.wait_for_url_contains("login")
        assert "login" in login_page.get_current_url().lower(), \
            "Без авторизации должен происходить переход на страницу входа"
