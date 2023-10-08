from pages.search import DuckDuckGoSearchPage
from pytest import mark


@mark.search
def test_duck_duck_go_search(browser):
    search = DuckDuckGoSearchPage(browser)
    # Give duckduckgo page is displayed
    search.load_search_page()
    # When the user searches for a "word"
    search.search_value('Alireza Soltani Jazi')
    # Then the result are shown for the "word"
