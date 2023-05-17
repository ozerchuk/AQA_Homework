import time

import pytest

from Homeworks.homework_19.pages.CheckboxPage import CheckboxPage

expand_list = ['home', 'desktop', 'documents', 'office', 'downloads']
marked_list = ['commands', 'general']


@pytest.mark.usefixtures('chrome')
class TestCheckBoxPage:

    def test_checkboxes(self):
        page = CheckboxPage(self.driver)
        page.open()
        page.expand_folders(*expand_list)
        page.mark_checkbox(*marked_list)






