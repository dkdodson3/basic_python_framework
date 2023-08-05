from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from tests.pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver, url_path="/abc/prospect-register/")

    @property
    def email_txt(self) -> WebElement:
        return self.get_shadow_page_component.find_element(By.CSS_SELECTOR, "#email")

    @property
    def submit_btn(self) -> WebElement:
        return self.get_shadow_page_component.find_element(By.CSS_SELECTOR, "#submit-button")

    def is_page_loaded(self) -> bool:
        return super().is_page_loaded() and self.email_txt is not None

    def submit_email(self, email_addr: str):
        """
        Submitting the email to register
        :param email_addr: str
        :return:
        """

        # Entering the new email and clicking on submit
        self.email_txt.send_keys(email_addr)
        self.submit_btn.click()
