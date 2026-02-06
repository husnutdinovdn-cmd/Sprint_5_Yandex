"""
Page Object для страницы профиля Stellar Burgers
"""
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):
    """Класс для работы со страницей профиля"""

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_page_load(self):
        """Ожидает загрузки страницы профиля"""
        self.wait_for_element_present(ProfilePageLocators.PAGE_TITLE)

    def click_logout_button(self):
        """Кликает на кнопку 'Выход'"""
        logout_button = self.wait_for_element_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        logout_button.click()

    def click_constructor_button(self):
        """Кликает на кнопку 'Конструктор'"""
        constructor_button = self.wait_for_element_clickable(ProfilePageLocators.CONSTRUCTOR_BUTTON)
        constructor_button.click()

    def click_logo(self):
        """Кликает на логотип Stellar Burgers"""
        logo = self.wait_for_element_clickable(ProfilePageLocators.LOGO)
        logo.click()

    def get_user_email(self):
        """Получает email пользователя из поля ввода"""
        try:
            email_input = self.wait_for_element_present(ProfilePageLocators.EMAIL_INPUT)
            return email_input.get_attribute('value')
        except Exception:
            return None

