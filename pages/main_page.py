import logging

from selenium.webdriver.common.by import By

from setup.base_setup import Base
from setup.button_web_element import Button

# log = logging.getLogger("MAIN_PAGE")


class MainPage(Base):
    MAIN_PAGE_TITE = "ROZETKA"
    login_input_selector = ""
    password_input_selector = ""
    sign_up_button_selector = ""

    def set_login(self, value: str) -> dict:
        field = self.driver.find_element(
            By.CSS_SELECTOR, self.login_input_selector
        )
        field.send_keys(value)

    def set_pass(self, value):
        field = self.driver.find_element(
            By.CSS_SELECTOR, self.password_input_selector
        )
        field.send_keys(value)

    def click_ok(self):
        Button(self.driver.find_element(
            By.CSS_SELECTOR, self.sign_up_button_selector)
        ).click()
