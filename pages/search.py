from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class DuckDuckGoSearchPage:
    # Arrange Data
    _url = 'https://www.duckduckgo.com'
    # Arrange Locators
    _search_input_field = (By.ID, 'searchbox_input')

    def __init__(self, browser: WebDriver, explicit_wait: float = 5):
        self._browser = browser
        self._explicit_wait = WebDriverWait(browser, explicit_wait)

    def load_search_page(self) -> None:
        self._browser.get(self._url)

    def search_value(self, phrase: str):
        search_input: WebElement = self._explicit_wait.until(
            expected_conditions.visibility_of_element_located(self._search_input_field)
        )
        search_input.send_keys(phrase + Keys.RETURN)
