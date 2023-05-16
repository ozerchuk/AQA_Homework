import pytest

from Homeworks.Homework_19.pages.RadiobuttonPage import RadioButtonPage

expand_list = ['home', 'desktop', 'documents', 'office', 'downloads']
marked_list = ['commands', 'general']


@pytest.mark.usefixtures('chrome')
class TestRadiobuttonPage:
    def test_radiobutton(self):
        page = RadioButtonPage(self.driver)
        page.open()
        page.radio_button_is_selected('yes')
        page.get_radio_buttons_info()
