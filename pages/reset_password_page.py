"""
Page Object для страницы сброса пароля Stellar Burgers
"""
from pages.base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordPageLocators


class ResetPasswordPage(BasePage):
    """Класс для работы со страницей сброса пароля"""

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_page_load(self):
        """Ожидает загрузки страницы сброса пароля"""
        self.wait_for_element_present(ResetPasswordPageLocators.PAGE_TITLE)

    def click_login_link(self):
        """Кликает на ссылку 'Войти'"""
        login_link = self.wait_for_element_clickable(ResetPasswordPageLocators.LOGIN_LINK)
        login_link.click()
