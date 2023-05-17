import time

import pytest

from Homeworks.homework_20.pages_.TextBox import TextBoxPage


@pytest.mark.usefixtures('chrome')
class TestTextboxPage:
    def test22(self):
        page = TextBoxPage(self.driver)
        page.open()
        page.fill_full_name_field('viktor')
        page.fill_email_field('viktor@gmail.com')
        page.fill_current_address('curr')
        page.fill_permanent_address('per')
        page.click_submit_button()
        time.sleep(10)

    def test_fullname(self):
        name = 'Viktor'
        page = TextBoxPage(self.driver).open()
        page.fill_full_name_field(name)
        page.click_submit_button()
        assert name in page.get_result_fullname()

    def test_email_positive(self):
        email = 'viktor@com.ua'
        page = TextBoxPage(self.driver).open()
        page.fill_email_field(email)
        page.click_submit_button()
        assert email in page.get_result_email()

    def test_email_negative(self):
        email = 'viktorcom.ua'
        page = TextBoxPage(self.driver).open()
        page.fill_full_name_field(email)
        page.click_submit_button()
        assert 'error' in page.get_email_field_element().get_attribute('class')

    def test_current_address(self):
        address = 'Viktor current addr'
        page = TextBoxPage(self.driver).open()
        page.fill_current_address(address)
        page.click_submit_button()
        assert address in page.get_result_current_address()

    def test_permanent_address(self):
        address = 'Viktor perm addr'
        page = TextBoxPage(self.driver).open()
        page.fill_permanent_address(address)
        page.click_submit_button()
        assert address == page.get_result_permanent_address()


