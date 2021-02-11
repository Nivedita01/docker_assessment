from Config.config import TestData
from Pages.MainPage import MainPage
from Tests.test_BasePage import TestBasePage


class TestSignInPage(TestBasePage):

    """POSITIVE TEST CASE"""
    """Testing if a valid user can enter the system, by providing right credentials"""
    """This assertion is passed"""

    def test_login(self):
        self.main_page = MainPage(self.driver)
        signin_page = self.main_page.click_signin_button()
        home_page = signin_page.do_login(TestData.DOCKER_ID, TestData.PASSWORD)
        assert home_page

    """NEGATIVE TEST CASE"""
    """Testing to check if invalid user is prompted with error page/message or not"""
    """This assertion is passed since I am asserting 'Invalid user' message."""

    def test_invalid_password(self):
        self.main_page = MainPage(self.driver)
        signin_page = self.main_page.click_signin_button()
        text = signin_page.do_invalid_login(TestData.INVALID_DOCKER_ID, TestData.INVALID_PASSWORD)
        assert text == TestData.INVALID_USER_MESSAGE

    # def test_signup_button_visible(self):
    #     self.main_page = MainPage(self.driver)
    #     signin_page = self.main_page.click_signin_button()
    #     flag = signin_page.is_signup_link_exists()
    #     assert flag
    #
    # def test_forgot_link_visible(self):
    #     self.main_page = MainPage(self.driver)
    #     signin_page = self.main_page.click_signin_button()
    #     flag = signin_page.is_forgot_link_exists()
    #     assert flag
    #
    # def test_login_page_title(self):
    #     self.main_page = MainPage(self.driver)
    #     signin_page = self.main_page.click_signin_button()
    #     title = signin_page.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
    #     assert title == TestData.LOGIN_PAGE_TITLE


