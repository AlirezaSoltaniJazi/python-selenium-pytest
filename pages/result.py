from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.logger_formatter import LOGGER


class DuckDuckGoResultPage:
    # Arrange Locators
    _RESULT_LINKS = (By.XPATH, '//ol//li//div//h2//a')
    _SEARCH_INPUT = (By.ID, 'search_form_input')

    def __init__(self, browser: WebDriver, explicit_wait: float = 5):
        self._browser = browser
        self._explicit_wait = WebDriverWait(browser, explicit_wait)

    def get_link_titles(self) -> list[str]:
        links: list[WebElement] = self._explicit_wait.until(
            expected_conditions.visibility_of_all_elements_located(self._RESULT_LINKS)
        )
        titles = [link.text for link in links]
        LOGGER.info('Result Titles', extra={'Titles': titles})
        return titles

    def get_search_input_text(self) -> str:
        search_input: WebElement = self._explicit_wait.until(
            expected_conditions.visibility_of_element_located(self._SEARCH_INPUT)
        )
        search_input_text = search_input.get_attribute('value')
        LOGGER.info('Search Input Data', extra={'Text': search_input_text})
        return search_input_text

    def get_page_title(self) -> str:
        page_title: str = self._browser.title
        LOGGER.info('Page Title', extra={'Title': page_title})
        return page_title
