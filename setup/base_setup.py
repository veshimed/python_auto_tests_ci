"""General setup for the tests.
Supported browsers: Chrome, Firefox, PhantomJS

"""
import os
import unittest

from selenium import webdriver

from utils.app_logger import get_logger
from utils.json_manager import get_setup_data

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_DIR = os.path.join(BASE_DIR, 'test_results')
LOG_PATH = '{}/test_res.txt'.format(RESULTS_DIR)


class Base(unittest.TestCase):
    """The base class to setup the test"""

    def setUp(self):
        """Setup required URL and browser"""

        self.log = get_logger('test')

        setup_data = get_setup_data()

        self.base_url = setup_data['base_url']
        browser = setup_data['browser'].lower()
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'phantomjs':
            self.driver = webdriver.PhantomJS()
        else:
            error = (
                '{0:s} is not a supported browser. Supported browsers: '
                'Chrome, Firefox, PhantomJS'.format(browser)
            )

            self.log.error(error)
            raise ValueError(error)
        self.log.info(
            'Setup data:\nURL: {0}\nBrowser: {1}'.format(
                self.base_url, browser
            )
        )
        self.log.info('Load main page')
        self.driver.get(self.base_url)

    def tearDown(self):
        """Close browser after test"""
        self.log.info('Close browser')
        self.driver.quit()
