"""General setup for the tests.
Supported browsers: Chrome, Firefox, PhantomJS

"""

import json
import os
import unittest

from pprint import pprint

from selenium import webdriver


class Base(unittest.TestCase):
    """The base class to setup the test"""

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    RES_DIR = os.path.join(BASE_DIR, 'resources')
    SUTUP_PATH = '{}/setup.json'.format(RES_DIR)

    def setUp(self):
        """Parse setup.json file to get required URL and browser"""

        with open(self.SUTUP_PATH) as data_file:
            data = json.load(data_file)
        pprint(data)

        self.base_url = data['base_url']
        browser = data['browser'].lower()
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'phantomjs':
            self.driver = webdriver.PhantomJS()
        else:
            raise ValueError(
                '{0:s} is not a supported browser. Supported browsers: '
                'Chrome, Firefox, PhantomJS'.format(browser)
            )

        self.driver.get(self.base_url)

    def tearDown(self):
        """Close browser after test"""
        self.driver.quit()
