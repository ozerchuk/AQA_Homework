import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from Homeworks.homework_20.pages_.Page_buttons import PageButtons


@pytest.mark.usefixtures('chrome')
class TestButtons:
    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = PageButtons(driver=self.driver)

    def test_double_click_button(self):
        self.page.open()
        self.page.button_doubleclick().doubleclick()
        assert 'double click' in self.page.get_button_doubleclick_message()
        pass

    def test_right_click_button(self):
        self.page.open()
        self.page.button_right_click().right_click()
        assert 'right click' in self.page.get_right_click_message()
        pass

    def test_dynamic_id_button(self):
        self.page.open()
        self.page.button_dynamic_id().click()
        assert 'dynamic click' in self.page.get_button_dynamic_id_message()
        pass
