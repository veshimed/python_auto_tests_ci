"""The test to check google search, just for fun :)"""

import unittest
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://www.google.com'
SEARCH = 'Love is...'
SEARCH_FIELD_NAME = "q"#'lst-ib'
IMAGES_BTN_XPATH = '//*[@id="hdtb-msb"]/div[2]/a'
TEST_IMAGE_XPATH = '//*[@id="rg_s"]/div[15]/a/img'


class GoogleSearchChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.screenshot_name = (
            'phantom.GoogleSearch.' + str(
                datetime.datetime.today()) + '.jpg'
        ).replace(':', '.').replace(' ', '-')

    def test_search_love_is(self):
        driver = self.driver
        driver.get(URL)

        self.assertIn("Google", driver.title)
        print('Google is loaded')
        driver.implicitly_wait(10)  # seconds

        search_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, SEARCH_FIELD_NAME))
        )

        print('Search field is loaded')

        search_field.clear()
        search_field.send_keys(SEARCH + Keys.RETURN)

        self.assertIn(SEARCH, driver.title)

        driver.save_screenshot(self.screenshot_name)
        print(self.screenshot_name)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
