"""
Page Object для страницы регистрации Stellar Burgers
"""
from pages.base_page import BasePage
from locators.registration_page_locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    """Класс для работы со страницей регистрации"""

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_page_load(self):
        """Ожидает загрузки страницы регистрации"""
        self.wait_for_element_present(RegistrationPageLocators.PAGE_TITLE)

    def enter_name(self, name):
        """Вводит имя в поле ввода"""
        name_input = self.wait_for_element_present(RegistrationPageLocators.NAME_INPUT)
        name_input.clear()
        name_input.send_keys(name)

    def enter_email(self, email):
        """Вводит email в поле ввода"""
        email_input = self.wait_for_element_present(RegistrationPageLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

    def enter_password(self, password):
        """Вводит пароль в поле ввода"""
        password_input = self.wait_for_element_present(RegistrationPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def click_register_button(self):
        """Кликает на кнопку 'Зарегистрироваться'"""
        register_button = self.wait_for_element_clickable(RegistrationPageLocators.REGISTER_BUTTON)
        register_button.click()

    def register(self, name, email, password):
        """Выполняет полный процесс регистрации"""
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_register_button()

    def click_login_link(self):
        """Кликает на ссылку 'Войти'"""
        login_link = self.wait_for_element_clickable(RegistrationPageLocators.LOGIN_LINK)
        login_link.click()

    def is_password_error_displayed(self):
        """Проверяет, отображается ли ошибка для некорректного пароля"""
        try:
            error = self.wait_for_element_present(RegistrationPageLocators.PASSWORD_ERROR)
            return error.is_displayed()
        except Exception:
            return False

    def get_error_message(self):
        """Получает текст сообщения об ошибке"""
        try:
            error = self.wait_for_element_present(RegistrationPageLocators.ERROR_MESSAGE)
            return error.text
        except Exception:
            return None

