import random

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from lib.settings import Settings as ConfigSettings
from tests.pages.pages import Pages


def get_random_integers():
    """
    Gets a random subset of integers
    :return:
    """
    return random.randint(100000000, 999999999)


@pytest.fixture(name="settings")
def get_settings() -> ConfigSettings:
    return ConfigSettings()


@pytest.fixture(name="email")
def get_email(settings) -> str:
    email_split = settings.email_addr.split("@")
    new_email = f"{email_split[0]}_{get_random_integers()}@{email_split[1]}"
    return new_email


@pytest.fixture(name="base_url")
def get_base_url(settings) -> str:
    base_url_str = f"{settings.url}"

    if settings.port:
        base_url_str = f"{base_url_str}:{settings.port}"

    return base_url_str


@pytest.fixture(name="driver")
def get_chrome_driver() -> WebDriver:
    """
    Creates a Chrome Driver
    :return: WebDriver
    """

    options = Options()
    options.add_experimental_option("prefs", {"profile.cookie_controls_mode": 0})
    driver = Chrome(options=options)

    yield driver
    driver.quit()


@pytest.fixture("pages")
def get_pages(driver) -> Pages:
    return Pages(driver=driver)
