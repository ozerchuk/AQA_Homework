import pytest

from Homeworks.homework_19.pages.RadiobuttonPage import RadioButtonPage


@pytest.mark.usefixtures('chrome')
class TestRadiobuttonPage:
    def test_radiobutton(self):
        page = RadioButtonPage(self.driver)
        page.open()
        page.radio_button_is_selected('yes')
        page.activate_yes_button('yes')
