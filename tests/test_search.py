from pytest import mark

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@mark.search
def test_duck_duck_go_search(browser):
    # Arrange
    search = DuckDuckGoSearchPage(browser, 10)
    result = DuckDuckGoResultPage(browser, 10)
    phrase = 'Alireza Soltani Jazi'

    # Act
    # Give duckduckgo page is displayed
    search.load_search_page()
    # When the user searches for a "word"
    search.search_value(phrase)
    # Then the result are shown for the "word"
    link_titles = result.get_link_titles()
    search_input_text = result.get_search_input_text()
    page_title = result.get_page_title()

    # Assert
    assert any(phrase in title for title in link_titles)
    assert phrase == search_input_text
    assert page_title.startswith(phrase)
