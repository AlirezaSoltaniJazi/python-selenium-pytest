from assertpy import assert_that
from pytest import mark

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@mark.search
def test_duck_duck_go_search(browser):
    # Arrange Section
    search = DuckDuckGoSearchPage(browser, 10)
    result = DuckDuckGoResultPage(browser, 10)
    url = 'https://www.duckduckgo.com'
    phrase = 'Alireza Soltani Jazi'

    # Act Section
    # Give duckduckgo page is displayed
    search.load_search_page(url)
    # When the user searches for a "word"
    search.search_value(phrase)
    # Then the result are shown for the "word"
    link_titles = result.get_link_titles()
    search_input_text = result.get_search_input_text()
    page_title = result.get_page_title()

    # Assert Section
    assert_that(any(phrase in title for title in link_titles), 'link titles').is_true()
    assert_that(search_input_text, 'search input text').is_equal_to(phrase)
    assert_that(page_title, 'page title').starts_with(phrase)
