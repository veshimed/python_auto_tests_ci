"""General setup for the tests.
Supported browsers: Chrome, Firefox, PhantomJS

"""

from selenium import webdriver

from utils.app_logger import get_logger
from utils.json_manager import get_setup_data


class Base():
    """The base class to setup the test"""

    log = get_logger('test')

    def setup(self):
        """Setup required URL and browser"""

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

    def teardown(self):
        """Close browser after test"""
        self.log.info('Close browser')
        self.driver.quit()
