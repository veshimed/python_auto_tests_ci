"""Simple test to test setup is working"""

import unittest

from pages.main_page import MainPage
from setup.base_setup import Base


class SimpleTest(Base):
    def test_setup(self):
        MainPage().set_login('sdfsd')
        MainPage().set_pass('sdf')
        MainPage().click_ok()
        assert 1 == MainPage.MAIN_PAGE_TITE

        # title = self.driver.title
        # self.assertTrue(
        #     'ROZETKA' in title,
        #     '"ROZETKA" not in title: {0:s}'.format(title)
        # )


if __name__ == "__main__":
    unittest.main()
