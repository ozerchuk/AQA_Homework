import time

import pytest

from Homeworks.homework_20.pages_.Radiobutton import RadioButtonPage


@pytest.mark.usefixtures('chrome')
class TestRadiobuttonPage:
    def test_activate_yes_button(self):
        page = RadioButtonPage(self.driver)
        page.open()
        page.activate_yes_button('yes')




