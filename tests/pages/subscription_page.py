from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class SubscriptionPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver, url_path="/abc/subscription/")

    @property
    def become_member(self):
        return self.get_shadow_page_component.find_element(By.CSS_SELECTOR, "#become-member")

    def is_page_loaded(self) -> bool:
        return super().is_page_loaded() and self.become_member is not None

