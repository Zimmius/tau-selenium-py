"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

import random
from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:
    SEARCH_INPUT = (By.ID, 'search_form_input')
    RESULT_LINKS = (By.CSS_SELECTOR, '[data-testid="result-title-a"]')
    MORE_RESULTS = (By.ID, 'rld-1')

    def __init__(self, browser):
        self.browser = browser

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def result_link_click(self):
        link_to_click = random.choice(self.browser.find_elements(*self.RESULT_LINKS))
        link_to_click.click()

    def show_more_results(self):
        more_results_button = self.browser.find_element(*self.MORE_RESULTS)
        more_results_button.click()

    def title(self):
        return self.browser.title

