"""
Локаторы для страницы сброса пароля Stellar Burgers
"""
from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    """Локаторы элементов страницы сброса пароля."""

    # Заголовок страницы сброса/восстановления пароля
    PAGE_TITLE = (By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]")

    # Ссылка/кнопка "Войти"
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")

