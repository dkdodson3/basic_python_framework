from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from .base_page import BasePage


class ABCPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver, url_path="/abc/")

    @property
    def signup_btn(self):
        return self.get_shadow_page_component.find_element(By.CSS_SELECTOR, "signup-button[aria-label='Sign Up for ABCmouse.com']")

    def is_page_loaded(self) -> bool:
        return super().is_page_loaded() and self.signup_btn is not None

    def signup(self):
        self.signup_btn.click()

