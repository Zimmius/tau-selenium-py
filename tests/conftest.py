"""
This module contains shared fixtures.
"""

import json
import pytest
import selenium.webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def config(scope='session'):
    # Read config file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):
    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        opts = Options()
        opts.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        b = selenium.webdriver.Firefox(options=opts)
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WevDriver instance for the cleanup
    b.quit()
