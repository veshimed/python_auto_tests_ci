"""General setup for the tests.
Supported browsers: Chrome,Firefox, PhantomJS

"""

import json

from pprint import pprint

import unittest

from selenium import webdriver


class Base(unittest.TestCase):
    """The base class to setup the test"""

    def setUp(self):
        """Parse setup.json file to get required URL and browser"""

        with open('setup.json') as data_file:
            data = json.load(data_file)
        pprint(data)

        self.base_url = data['base_url']
        browser = data['browser'].lower()
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'PhantomJS':
            self.driver = webdriver.PhantomJS()
        else:
            raise ValueError(
                '{0:s} is not a supported browser. Supported browsers: Chrome,'
                'Firefox, PhantomJS'.format(browser)
            )

        self.driver.get(self.base_url)

    def tearDown(self):
        self.driver.quit()
