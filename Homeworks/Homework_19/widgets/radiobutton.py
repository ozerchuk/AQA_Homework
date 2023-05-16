from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RadioButton:
    def __init__(self, driver: WebDriver = None, locator: tuple = None, name: str = None):
        self.driver = driver
        self.locator = locator
        self.by, self.loc = self.locator
        if name:
            self.name: str = name
            self.loc = self.loc.format(self.name)
            pass

    def select(self, name: str = None) -> None:
        if self.name:
            self.driver.find_element(self.by, self.loc).click()
        else:
            self.driver.find_element(*self.locator).click()

    def is_selected(self, name: str) -> bool:
        element = self.driver.find_element(self.by, self.loc)
        return element.is_selected()
