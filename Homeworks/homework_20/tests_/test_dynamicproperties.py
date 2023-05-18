import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from Homeworks.homework_20.pages_.DynamicProperties import PageDynamicProperties


@pytest.mark.usefixtures('chrome')
class TestDynamicProperties:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = PageDynamicProperties(self.driver)
        self.page.open()

    def test_appeared_button(self):
        button = self.page.button_appeared()
        assert button.is_displayed()

    def test_enabled_disabled_button(self):
        button = self.page.button_disabled_enabled()
        assert button.is_enabled()

    def test_changed_color_button(self):
        button = self.page.button_color_changed()
        assert button

#   def setup_method(self):
#       self.driver: WebDriver = self.driver
#       self.page = PageDynamicProperties(self.driver)
#       self.page.open()
#
#    def test_is_button_enable(self):
#       page = PageDynamicProperties(self.driver).open()
#       self.page.open()
#       button: WebElement = page.button_disabled_enabled()
#       WebDriverWait(self.driver, 7).until(ec.element_to_be_clickable(button))
#       assert button.is_enabled()
#       button.click()
#
#    def test_is_button_shown(self):
#       page = PageDynamicProperties(self.driver).open()
#       self.page.open()
#       button: WebElement = page.button_invisible_visible()
#       button.click()
