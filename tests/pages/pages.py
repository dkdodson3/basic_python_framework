from selenium.webdriver.chrome.webdriver import WebDriver
from tests.pages.abc_page import ABCPage
from tests.pages.register_page import RegisterPage
from tests.pages.subscription_page import SubscriptionPage


class Pages:
    def __init__(self, driver: WebDriver):
        self.abc = ABCPage(driver=driver)
        self.register = RegisterPage(driver=driver)
        self.subscription = SubscriptionPage(driver=driver)
