import pytest

from Homeworks.homework_19.pages.RadiobuttonPage import RadioButtonPage


@pytest.mark.usefixtures('chrome')
class TestRadiobuttonPage:
    def test_activate_yes_button(self):
        page = RadioButtonPage(self.driver)
        page.open()
        page.activate_yes_button('yes')

    def test_radio_button_is_selected(self):
        page = RadioButtonPage(self.driver)
        page.radio_button_is_selected('yes')



