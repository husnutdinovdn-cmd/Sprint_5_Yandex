"""
Локаторы для страницы восстановления пароля Stellar Burgers
"""
from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    """Локаторы элементов страницы восстановления пароля."""

    # Заголовок страницы восстановления пароля
    PAGE_TITLE = (By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]")

    # Ссылка/кнопка "Войти"
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")

