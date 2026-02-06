"""
Фикстуры pytest для автотестов Stellar Burgers
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.data_generator import generate_test_data


def pytest_addoption(parser):
    """Добавляет опции командной строки для pytest"""
    parser.addoption('--browser', action='store', default='chrome',
                     help='Выбор браузера: chrome или firefox')
    parser.addoption('--headless', action='store_true', default=False,
                     help='Запуск в headless режиме')


@pytest.fixture(scope='function')
def browser(request):
    """
    Фикстура для создания и закрытия браузера
    
    Args:
        request: объект запроса pytest для доступа к опциям
    
    Yields:
        WebDriver: экземпляр драйвера браузера
    """
    browser_name = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')
    
    if browser_name == 'chrome':
        chrome_options = ChromeOptions()
        if headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920,1080')
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    elif browser_name == 'firefox':
        firefox_options = FirefoxOptions()
        if headless:
            firefox_options.add_argument('--headless')
        firefox_options.add_argument('--width=1920')
        firefox_options.add_argument('--height=1080')
        
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)
    else:
        raise ValueError(f'Неподдерживаемый браузер: {browser_name}')
    
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def generate_test_data_fixture():
    """
    Фикстура для генерации тестовых данных
    
    Returns:
        dict: словарь с тестовыми данными (name, email, password)
    """
    return generate_test_data()


@pytest.fixture
def registered_user(browser):
    """
    Фикстура для создания зарегистрированного пользователя
    
    Args:
        browser: фикстура браузера
    
    Returns:
        dict: данные зарегистрированного пользователя (name, email, password)
    """
    from pages.main_page import MainPage
    from pages.registration_page import RegistrationPage
    from pages.login_page import LoginPage
    
    # Генерируем тестовые данные
    test_data = generate_test_data()
    
    # Регистрируем пользователя
    main_page = MainPage(browser)
    main_page.open()
    main_page.click_login_button()
    
    login_page = LoginPage(browser)
    login_page.wait_for_page_load()
    login_page.click_register_link()
    
    registration_page = RegistrationPage(browser)
    registration_page.wait_for_page_load()
    registration_page.register(
        test_data['name'],
        test_data['email'],
        test_data['password']
    )
    
    # Ждем перехода на страницу входа после регистрации
    login_page.wait_for_page_load()
    
    return test_data


@pytest.fixture
def logged_in_user(browser, registered_user):
    """
    Фикстура для создания авторизованного пользователя
    
    Args:
        browser: фикстура браузера
        registered_user: фикстура зарегистрированного пользователя
    
    Returns:
        dict: данные авторизованного пользователя (name, email, password)
    """
    from pages.main_page import MainPage
    from pages.login_page import LoginPage
    
    # Выполняем вход
    main_page = MainPage(browser)
    main_page.open()
    main_page.click_login_button()
    
    login_page = LoginPage(browser)
    login_page.wait_for_page_load()
    login_page.login(registered_user['email'], registered_user['password'])
    
    # Ждем перехода на главную страницу
    main_page.wait_for_page_load()
    
    return registered_user
