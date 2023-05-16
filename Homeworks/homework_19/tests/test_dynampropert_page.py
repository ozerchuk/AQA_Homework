import pytest
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Homeworks.homework_19.pages.DynamicPropertiesPage import PageDynamicProperties


@pytest.mark.usefixtures('chrome')
class TestDynamicPropertiesPage:
    def test_is_button_enable(self):
        page = PageDynamicProperties(self.driver).open()
        button: WebElement = page.button_disabled_enabled()
        WebDriverWait(self.driver, 7).until(ec.element_to_be_clickable(button))
        assert button.is_enabled()
        button.click()

    def test_is_button_shown(self):
        page = PageDynamicProperties(self.driver).open()
        button: WebElement = page.button_invisible_visible()
        button.click()

