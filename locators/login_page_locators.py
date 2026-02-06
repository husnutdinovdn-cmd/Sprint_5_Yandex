"""
Локаторы для страницы входа Stellar Burgers
"""
from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Локаторы элементов страницы входа"""
    
    # Заголовок страницы входа
    PAGE_TITLE = (By.XPATH, "//h2[contains(text(), 'Вход')]")
    
    # Поле ввода email
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    
    # Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, "//label[contains(text(), 'Пароль')]/following-sibling::input")
    
    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    
    # Кнопка "Зарегистрироваться" (ссылка на страницу регистрации)
    REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
    
    # Кнопка "Восстановить пароль"
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
