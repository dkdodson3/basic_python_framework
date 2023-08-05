from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from lib.settings import Settings
from tests.pages.common_functions import CommonFunctions


class BasePage:
    common_func: CommonFunctions = CommonFunctions()

    def __init__(self, driver: WebDriver, url_path: str):
        self.settings = Settings()
        self.driver: WebDriver = driver
        self.url_path = url_path
        self.url = f"{self.settings.url}/{url_path}"

    @property
    def get_shadow_route_view(self) -> WebElement:
        return self.common_func.get_shadow_route_view(driver=self.driver)

    @property
    def get_shadow_page_component(self) -> WebElement:
        return self.common_func.get_shadow_page_component(driver=self.driver, shadow_element=self.get_shadow_route_view)

    def load(self):
        self.driver.get(url=self.url)

    def is_page_loaded(self) -> bool:
        return self.common_func.wait_for_url(driver=self.driver, url=self.url) \
            and self.get_shadow_route_view is not None
