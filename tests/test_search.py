"""
These tests cover DuckDuckGo searches.
"""
import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckSearchPage

# Testing search with RETURN key and different phrases
@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for phrase
    search_page.search(f'"{phrase}"')

    # Then the search result query is phrase
    assert f'"{phrase}"' == result_page.search_input_value()

    # And the search result links pertain to phrase
    for title in result_page.result_link_titles():
        assert phrase.lower() in title.lower()

    # And the search result title contains phrase
    assert phrase in result_page.title()


# Testing search with search button
def test_button_duckduckgo_search(browser):
    search_page = DuckDuckSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    phrase = "panda"

    # Given the duckduckgo homepage is displayed
    search_page.load()

    # When the user searches for phrase using search button
    search_page.search_by_button(f'"{phrase}"')

    # Then result page search input contains phrase
    assert f'"{phrase}"' == result_page.search_input_value()

    # And the result links contain phrase
    for title in result_page.result_link_titles():
        assert phrase.lower() in title.lower()

    # And the result page title contains phrase
    assert phrase in result_page.title()


# Testing clicking search result click
def test_result_link_click(browser):
    search_page = DuckDuckSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    phrase = 'panda'

    # Given the duckduckgo homepage is displayed
    search_page.load()

    # When the user searches for phrase using return key
    search_page.search(f'"{phrase}"')

    # Then the result links contain phrase
    for title in result_page.result_link_titles():
        assert phrase.lower() in title.lower()

    # When user clicks search result link
    result_page.result_link_click()

    # Then browsers url does not contain https://duckduckgo.com
    assert search_page.URL not in browser.current_url


# Testing "More results" button on the search page
def test_more_results_button(browser):
    search_page = DuckDuckSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    phrase = 'panda'

    # Given the duckduckgo homepage is displayed
    search_page.load()

    # When the user searches for phrase using return key
    search_page.search(f'"{phrase}"')

    # Then save count of the result links before more results is clicked
    old_link_count = len(result_page.result_link_titles())

    # When "more results" button is clicked
    result_page.show_more_results()

    # Then new results count > than old results count
    new_link_count = len(result_page.result_link_titles())
    assert  new_link_count > old_link_count