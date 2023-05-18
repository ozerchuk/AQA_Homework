from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from Homeworks.homework_20.helper.elements import get_appeared_element


class PageDynamicProperties:
    URL = 'https://demoqa.com/dynamic-properties'
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.disabled_enabled_button_loc = (By.CSS_SELECTOR, 'button#enableAfter')
        self.invisible_visible_button_loc = (By.CSS_SELECTOR, 'button#visibleAfter')
        self.color_changed_button_loc = (By.CSS_SELECTOR, 'button#colorChange')
        self.color_changed_button_attribute_loc = ('class', 'text-danger btn btn-primary')

    def open(self) -> 'PageDynamicProperties':
        self.driver.get(self.URL)
        return self

    def button_appeared(self) -> WebElement:
        button = get_appeared_element(self.driver, self.invisible_visible_button_loc, 5, poll=0.2)
        return button

    def button_disabled_enabled(self) -> WebElement:
        button = self.driver.find_element(*self.disabled_enabled_button_loc)
        WebDriverWait(self.driver, 7).until(ec.element_to_be_clickable(button))
        return button

    def button_color_changed(self) -> WebElement:
        button = self.driver.find_element(*self.color_changed_button_loc)
        wait = WebDriverWait(self.driver, 6)
        wait.until(ec.text_to_be_present_in_element_attribute(self.color_changed_button_loc,
                                                              *self.color_changed_button_attribute_loc))
        return button
