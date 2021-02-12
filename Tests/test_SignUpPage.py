from Config.config import TestData
from Pages.MainPage import MainPage
from Tests.test_BasePage import TestBasePage


class TestSignUpPage(TestBasePage):

    """NEGATIVE TEST CASE"""
    """Test to verify if copying of password can be performed or not"""
    """In this scenario, I have copied the password from password field and tried pasting into email field and then 
    read the email field and performed an assert """
    """This assertion failed since there is no password copied into the email field."""
    def test_copy_password(self):
        self.main_page = MainPage(self.driver)
        signin_page = self.main_page.click_signin_button()
        signup_page = signin_page.click_signup_link()
        text = signup_page.copy_password_text(TestData.PASS_2)
        assert text == TestData.PASS_2, "EXPECTED: testtest123, ACTUAL: ' '"
