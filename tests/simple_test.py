"""Simple test to test setup is working"""

import unittest

from pages.main_page import MainPage
from setup.base_setup import Base


class SimpleTest(Base):
    def test_setup_positive(self):
        title = MainPage().MAIN_PAGE_TITE

        found_title = self.driver.title
        self.assertTrue(
            title in found_title,
            '{0} not in title: {1}'.format(title, found_title)
        )

    def test_setup_negative(self):
        title = MainPage().MAIN_PAGE_TITE

        found_title = self.driver.title
        self.assertTrue(
            (title + '-negative_test') in found_title,
            '{0} not in title: {1}'.format(title, found_title)
        )

if __name__ == "__main__":
    unittest.main()
