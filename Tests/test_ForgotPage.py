from Config.config import TestData
from Pages.MainPage import MainPage
from Tests.test_BasePage import TestBasePage


class TestForgotPage(TestBasePage):

    """NEGATIVE TEST CASE"""
    """Test to check if no email address is entered for resetting password, the page shows appropriate message"""
    """In this scenario, after clicking on Forgot Password Link, I have clicked on Send button without providing any 
    details and validated the message received from the website """

    def test_no_email_entered(self):
        self.main_page = MainPage(self.driver)
        signin_page = self.main_page.click_signin_button()
        if signin_page.is_forgot_link_exists():
            forgot_page = signin_page.click_forgot_link()
            text = forgot_page.click_send_no_email()
            assert text == TestData.INVALID_EMAIL_ADDRESS

    """VERIFYING TITLE OF FORGOT PASSWORD PAGE"""
    """Test to check if title of Landing page of Forgot Password page is as intended"""

    def test_forgot_link(self):
        self.main_page = MainPage(self.driver)
        signin_page = self.main_page.click_signin_button()
        if signin_page.is_forgot_link_exists():
            forgot_page = signin_page.click_forgot_link()
            title = forgot_page.get_title(TestData.RESET_PASSWORD_TITLE)
            assert title == TestData.RESET_PASSWORD_TITLE
