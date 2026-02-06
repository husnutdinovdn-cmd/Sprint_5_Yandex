"""
Локаторы для страницы профиля (личного кабинета) Stellar Burgers
"""
from selenium.webdriver.common.by import By


class ProfilePageLocators:
    """Локаторы элементов страницы профиля"""
    
    # Заголовок страницы профиля
    PAGE_TITLE = (By.XPATH, "//a[contains(text(), 'Профиль')]")
    
    # Кнопка "Выход"
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    
    # Поле ввода имени в профиле
    NAME_INPUT = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input")
    
    # Поле ввода email в профиле
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Логин')]/following-sibling::input")
    
    # Кнопка "Конструктор" в меню
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    
    # Логотип Stellar Burgers
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
