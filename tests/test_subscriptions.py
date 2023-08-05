from selenium.webdriver.chrome.webdriver import WebDriver

from lib.constants import Constants
from tests.pages.pages import Pages


def test_subscription_text(driver: WebDriver, pages: Pages, email):
    # Wait until we are on the abc page and signup
    pages.abc.load()
    assert pages.abc.is_page_loaded() is True
    pages.abc.signup()

    # Wait until we are on the registration page and submit email
    assert pages.register.is_page_loaded() is True
    pages.register.submit_email(email_addr=email)

    # Wait until we are on the subscription page and verify become member text
    assert pages.subscription.is_page_loaded() is True
    assert pages.subscription.become_member.text == Constants.SUBSCRIPTION_BECOME_MEMBER_TEXT, \
        "Did not find the correct text for become a member"



