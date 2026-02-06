"""
Локаторы для главной страницы Stellar Burgers
"""
from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы элементов главной страницы"""
    
    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    
    # Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный кабинет')]")
    
    # Логотип Stellar Burgers
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    
    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    
    # Раздел "Булки" в конструкторе
    BUNS_SECTION = (By.XPATH, "//span[contains(text(), 'Булки')]/parent::div")
    
    # Раздел "Соусы" в конструкторе
    SAUCES_SECTION = (By.XPATH, "//span[contains(text(), 'Соусы')]/parent::div")
    
    # Раздел "Начинки" в конструкторе
    FILLINGS_SECTION = (By.XPATH, "//span[contains(text(), 'Начинки')]/parent::div")
    
    # Активный раздел (для проверки)
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
    
    # Заголовок страницы
    PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")
