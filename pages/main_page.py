"""
Page Object для главной страницы Stellar Burgers
"""
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    """Класс для работы с главной страницей"""

    def __init__(self, driver):
        super().__init__(driver, base_url="https://stellarburgers.nomoreparties.site/")

    def open(self):
        """Открывает главную страницу"""
        super().open()
        self.wait_for_page_load()

    def wait_for_page_load(self):
        """Ожидает загрузки главной страницы"""
        self.wait_for_element_present(MainPageLocators.PAGE_TITLE)

    def click_login_button(self):
        """Кликает на кнопку 'Войти в аккаунт'"""
        login_button = self.wait_for_element_clickable(MainPageLocators.LOGIN_BUTTON)
        login_button.click()

    def click_personal_account_button(self):
        """Кликает на кнопку 'Личный кабинет'"""
        account_button = self.wait_for_element_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        account_button.click()

    def click_constructor_button(self):
        """Кликает на кнопку 'Конструктор'"""
        constructor_button = self.wait_for_element_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        constructor_button.click()

    def click_logo(self):
        """Кликает на логотип Stellar Burgers"""
        logo = self.wait_for_element_clickable(MainPageLocators.LOGO)
        logo.click()

    def click_buns_section(self):
        """Кликает на раздел 'Булки' в конструкторе"""
        buns_section = self.wait_for_element_clickable(MainPageLocators.BUNS_SECTION)
        buns_section.click()

    def click_sauces_section(self):
        """Кликает на раздел 'Соусы' в конструкторе"""
        sauces_section = self.wait_for_element_clickable(MainPageLocators.SAUCES_SECTION)
        sauces_section.click()

    def click_fillings_section(self):
        """Кликает на раздел 'Начинки' в конструкторе"""
        fillings_section = self.wait_for_element_clickable(MainPageLocators.FILLINGS_SECTION)
        fillings_section.click()

    def is_buns_section_active(self):
        """Проверяет, активен ли раздел 'Булки'"""
        try:
            active_section = self.wait_for_element_present(MainPageLocators.ACTIVE_SECTION)
            return "Булки" in active_section.text
        except Exception:
            return False

    def is_sauces_section_active(self):
        """Проверяет, активен ли раздел 'Соусы'"""
        try:
            active_section = self.wait_for_element_present(MainPageLocators.ACTIVE_SECTION)
            return "Соусы" in active_section.text
        except Exception:
            return False

    def is_fillings_section_active(self):
        """Проверяет, активен ли раздел 'Начинки'"""
        try:
            active_section = self.wait_for_element_present(MainPageLocators.ACTIVE_SECTION)
            return "Начинки" in active_section.text
        except Exception:
            return False

