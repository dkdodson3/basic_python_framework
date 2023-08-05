from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CommonFunctions:
    @staticmethod
    def get_shadow_root(*, driver: WebDriver, element: WebElement, array_num: int = 0) -> WebElement:
        """
        Gets the shadowroot for a speecific dome
        :param driver: WebDriver
        :param element: WebElement
        :param array_num: int
        :return: WebElement
        """

        return driver.execute_script(f"return arguments['{array_num}'].shadowRoot", element)

    @staticmethod
    def get_shadow_route_view(driver: WebDriver) -> WebElement:
        """
        Get the shadow_route_view
        :param driver: WebDriver
        :return: WebElement
        """
        from selenium.webdriver.common.by import By

        route_view = driver.find_element(By.CSS_SELECTOR, "route-view[class='loaded']")
        return CommonFunctions.get_shadow_root(driver=driver, element=route_view)

    @staticmethod
    def get_shadow_page_component(driver: WebDriver, shadow_element: WebElement = None) -> WebElement:
        """
        Get the shadow page_component
        :param driver: WebDriver
        :param shadow_element: WebElement
        :return: WebElement
        """

        from selenium.webdriver.common.by import By
        if shadow_element is None:
            shadow_element: WebElement = CommonFunctions.get_shadow_route_view(driver=driver)

        page_component = shadow_element.find_element(By.CSS_SELECTOR, "#page-component")
        return CommonFunctions.get_shadow_root(driver=driver, element=page_component)

    @staticmethod
    def wait_until_visible(*, driver: WebDriver, selector: str, shadow_element: WebElement, timeout=10):
        """
        Wait for a visible element based upon a selector and a shadow element
        :param driver: WebDriver
        :param selector: str
        :param shadow_element: WebElement
        :param timeout: int
        :return:
        """

        return WebDriverWait(driver, timeout=timeout).until(
            EC.visibility_of(shadow_element.find_element((By.CSS_SELECTOR, selector)))
        )

    @staticmethod
    def wait_for_url(driver: WebDriver, url: str, timeout: int = 10) -> bool:
        """
        Wait for the curl to change
        :param driver: WebDriver
        :param url: url
        :param timeout: int
        :return: bool
        """

        try:
            WebDriverWait(driver, timeout).until(EC.url_matches(url))
            return True
        except TimeoutException:
            return False
