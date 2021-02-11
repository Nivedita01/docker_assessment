from Pages.MainPage import MainPage
from Tests.test_BasePage import TestBasePage


class TestMainPage(TestBasePage):

    def test_click_signin(self):
        self.mainPage = MainPage(self.driver)
        signin_page = self.mainPage.click_signin_button()
        assert signin_page

