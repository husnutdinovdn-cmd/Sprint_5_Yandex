"""
Локаторы для страницы регистрации Stellar Burgers
"""
from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    """Локаторы элементов страницы регистрации"""
    
    # Заголовок страницы регистрации
    PAGE_TITLE = (By.XPATH, "//h2[contains(text(), 'Регистрация')]")
    
    # Поле ввода имени
    NAME_INPUT = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input")
    
    # Поле ввода email
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    
    # Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, "//label[contains(text(), 'Пароль')]/following-sibling::input")
    
    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    
    # Кнопка "Войти" (ссылка на страницу входа)
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")
    
    # Сообщение об ошибке для некорректного пароля
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error') and contains(text(), 'Некорректный пароль')]")
    
    # Общее сообщение об ошибке
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")
