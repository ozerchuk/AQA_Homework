import time

from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def get_appeared_element(
        driver: WebDriver,
        locator: tuple,
        timeout: int,
        poll: float | int = 0.1) -> WebElement:
    """
    :param driver: WebDriver
    :param locator: tuple with By. Example: (By.XPATH, "//div[@id]")
    :param timeout: Max time to wait for element to be enabled
    :param poll: Time to sleep in loop
    :return: WebElement if it presents in DOM tree
    """
    end_time = time.monotonic() + timeout
    while time.monotonic() <= end_time:
        try:
            element = driver.find_element(*locator)
            return element
        except NoSuchElementException:
            time.sleep(poll)
            continue
    raise
