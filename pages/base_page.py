"""
Базовый класс Page Object для приложения Stellar Burgers.
Содержит общие методы работы с драйвером и WebDriverWait.
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех Page Object-классов."""

    def __init__(self, driver, base_url: str | None = None, timeout: int = 10):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str | None = None):
        """Открывает указанную страницу (если url не передан — используется base_url)."""
        target_url = url or self.base_url
        if not target_url:
            raise ValueError("URL для открытия страницы не задан")
        self.driver.get(target_url)

    def wait_for_element_present(self, locator):
        """Ожидает появления элемента в DOM и возвращает его."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        """Ожидает, когда элемент станет кликабельным, и возвращает его."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_url_contains(self, text: str):
        """Ожидает, что текущий URL будет содержать указанный текст."""
        return self.wait.until(EC.url_contains(text))

    def get_current_url(self) -> str:
        """Возвращает текущий URL браузера."""
        return self.driver.current_url

