"""The test to check google search, just for fun :)"""

import unittest
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "https://www.google.com"
SEARCH = "Love is..."


class GoogleSearchChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.screen_name = (
            'Screenshots/Chrome.GoogleSearch.' + str(datetime.datetime.today()) + '.jpg'
        ).replace(':', '.')

    def test_search_love_is(self):
        driver = self.driver
        driver.get(URL)

        self.assertIn("Google", driver.title)
        search_field = driver.find_element_by_id("lst-ib")
        search_field.clear()
        search_field.send_keys(SEARCH + Keys.RETURN)

        driver.implicitly_wait(10)  # seconds
        img = driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[2]/a').click()
        driver.implicitly_wait(10)  # seconds
        driver.find_element_by_xpath('//*[@id="rg_s"]/div[15]/a/img')
        if ("No result found" in driver.page_source):
            driver.save_screenshot(self.screen_name)
            print(self.screen_name)
            self.fail()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
