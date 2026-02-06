"""
Page Object для страницы входа Stellar Burgers
"""
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    """Класс для работы со страницей входа"""

    def __init__(self, driver):
        # Для логин-страницы базовый URL может быть полезен в проверках
        super().__init__(driver, base_url="https://stellarburgers.nomoreparties.site/login")

    def wait_for_page_load(self):
        """Ожидает загрузки страницы входа"""
        self.wait_for_element_present(LoginPageLocators.PAGE_TITLE)

    def enter_email(self, email):
        """Вводит email в поле ввода"""
        email_input = self.wait_for_element_present(LoginPageLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

    def enter_password(self, password):
        """Вводит пароль в поле ввода"""
        password_input = self.wait_for_element_present(LoginPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def click_login_button(self):
        """Кликает на кнопку 'Войти'"""
        login_button = self.wait_for_element_clickable(LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def login(self, email, password):
        """Выполняет полный процесс входа"""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def click_register_link(self):
        """Кликает на ссылку 'Зарегистрироваться'"""
        register_link = self.wait_for_element_clickable(LoginPageLocators.REGISTER_LINK)
        register_link.click()

    def click_forgot_password_link(self):
        """Кликает на ссылку 'Восстановить пароль'"""
        forgot_password_link = self.wait_for_element_clickable(LoginPageLocators.FORGOT_PASSWORD_LINK)
        forgot_password_link.click()

