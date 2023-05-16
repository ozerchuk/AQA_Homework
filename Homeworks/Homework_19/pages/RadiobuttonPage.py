from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Homeworks.Homework_19.widgets.button import Button


class RadioButtonPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = 'https://demoqa.com/radio-button'

    def open(self) -> 'RadioButtonPage':
        self.driver.get(self.url)
        return self

    def activate_yes_button(self, name):
        yes_button = self.driver.find_element(By.XPATH,
                                              f'//label[contains(@for, "{name}Radio")]')
        Button.click(yes_button)

    def radio_button_is_selected(self, name) -> bool:
        element = self.driver.find_element(By.XPATH,
                                           f'//label[contains(@for, "{name}Radio")]//ancestor::div[contains(@class, "radio")]/input')
        return element.is_selected()

    def get_radio_buttons_info(self):
        radio_buttons = self.driver.find_elements(By.CSS_SELECTOR, '.custom-control-label')
        buttons_info = {}

        for button in radio_buttons:
            button_name = button.text.strip()
            is_selected = button.find_element(By.XPATH, ".//preceding-sibling::input").is_selected()
            is_active = button.find_element(By.XPATH, ".//preceding-sibling::input").get_attribute("aria-checked") == "true"

            buttons_info[button_name] = {
                'Does the button is switch on': is_selected,
                'Does the button is active': is_active
            }

        return buttons_info
