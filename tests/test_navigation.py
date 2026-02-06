"""
Тесты для навигации по приложению Stellar Burgers
"""
import pytest
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestNavigation:
    """Класс тестов для навигации"""
    
    def test_navigate_to_personal_account(self, browser, logged_in_user):
        """
        Тест перехода в личный кабинет по клику на кнопку "Личный кабинет"
        """
        # Открываем главную страницу (уже авторизованы)
        main_page = MainPage(browser)
        main_page.open()
        main_page.wait_for_page_load()
        
        # Переходим в личный кабинет
        main_page.click_personal_account_button()
        profile_page = ProfilePage(browser)
        profile_page.wait_for_page_load()
        
        # Проверяем, что мы на странице профиля
        profile_page.wait_for_url_contains("profile")
        assert "profile" in profile_page.get_current_url().lower(), \
            "Должен произойти переход в личный кабинет"
        
        # Проверяем, что email пользователя отображается
        user_email = profile_page.get_user_email()
        assert user_email == logged_in_user['email'], \
            f"Email пользователя должен совпадать: ожидалось {logged_in_user['email']}, получено {user_email}"
    
    def test_navigate_from_profile_to_constructor_via_button(self, browser, logged_in_user):
        """
        Тест перехода из личного кабинета в конструктор через кнопку "Конструктор"
        """
        # Открываем главную страницу (уже авторизованы)
        main_page = MainPage(browser)
        main_page.open()
        main_page.wait_for_page_load()
        
        # Переходим в личный кабинет
        main_page.click_personal_account_button()
        profile_page = ProfilePage(browser)
        profile_page.wait_for_page_load()
        
        # Переходим в конструктор через кнопку "Конструктор"
        profile_page.click_constructor_button()
        main_page.wait_for_page_load()
        
        # Проверяем, что мы вернулись на главную страницу
        main_page.wait_for_url_contains("stellarburgers.nomoreparties.site")
        current_url = main_page.get_current_url()
        assert "stellarburgers.nomoreparties.site" in current_url and \
               "profile" not in current_url.lower(), \
            "Должен произойти переход в конструктор (главную страницу)"
    
    def test_navigate_from_profile_to_constructor_via_logo(self, browser, logged_in_user):
        """
        Тест перехода из личного кабинета в конструктор через логотип Stellar Burgers
        """
        # Открываем главную страницу (уже авторизованы)
        main_page = MainPage(browser)
        main_page.open()
        main_page.wait_for_page_load()
        
        # Переходим в личный кабинет
        main_page.click_personal_account_button()
        profile_page = ProfilePage(browser)
        profile_page.wait_for_page_load()
        
        # Переходим в конструктор через логотип
        profile_page.click_logo()
        main_page.wait_for_page_load()
        
        # Проверяем, что мы вернулись на главную страницу
        main_page.wait_for_url_contains("stellarburgers.nomoreparties.site")
        current_url = main_page.get_current_url()
        assert "stellarburgers.nomoreparties.site" in current_url and \
               "profile" not in current_url.lower(), \
            "Должен произойти переход в конструктор (главную страницу) через логотип"
