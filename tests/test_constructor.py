"""
Тесты для конструктора бургеров Stellar Burgers
"""
import pytest
from pages.main_page import MainPage


class TestConstructor:
    """Класс тестов для конструктора бургеров"""
    
    def test_switch_to_buns_section(self, browser):
        """
        Тест перехода к разделу "Булки" в конструкторе
        """
        # Открываем главную страницу
        main_page = MainPage(browser)
        main_page.open()
        main_page.wait_for_page_load()
        
        # Переходим к разделу "Булки"
        main_page.click_buns_section()
        
        # Проверяем, что раздел "Булки" активен
        assert main_page.is_buns_section_active(), \
            "Раздел 'Булки' должен быть активным"
    
    def test_switch_to_sauces_section(self, browser):
        """
        Тест перехода к разделу "Соусы" в конструкторе
        """
        # Открываем главную страницу
        main_page = MainPage(browser)
        main_page.open()
        main_page.wait_for_page_load()
        
        # Переходим к разделу "Соусы"
        main_page.click_sauces_section()
        
        # Проверяем, что раздел "Соусы" активен
        assert main_page.is_sauces_section_active(), \
            "Раздел 'Соусы' должен быть активным"
    
    def test_switch_to_fillings_section(self, browser):
        """
        Тест перехода к разделу "Начинки" в конструкторе
        """
        # Открываем главную страницу
        main_page = MainPage(browser)
        main_page.open()
        main_page.wait_for_page_load()
        
        # Переходим к разделу "Начинки"
        main_page.click_fillings_section()
        
        # Проверяем, что раздел "Начинки" активен
        assert main_page.is_fillings_section_active(), \
            "Раздел 'Начинки' должен быть активным"
    
    def test_switch_between_sections(self, browser):
        """
        Тест переключения между разделами конструктора
        """
        # Открываем главную страницу
        main_page = MainPage(browser)
        main_page.open()
        main_page.wait_for_page_load()
        
        # Переходим к разделу "Соусы"
        main_page.click_sauces_section()
        assert main_page.is_sauces_section_active(), \
            "Раздел 'Соусы' должен быть активным"
        
        # Переходим к разделу "Начинки"
        main_page.click_fillings_section()
        assert main_page.is_fillings_section_active(), \
            "Раздел 'Начинки' должен быть активным"
        
        # Переходим к разделу "Булки"
        main_page.click_buns_section()
        assert main_page.is_buns_section_active(), \
            "Раздел 'Булки' должен быть активным"
