from Config.config import TestData
from Pages.MainPage import MainPage
from Tests.test_BasePage import TestBasePage


class TestHomePage(TestBasePage):

    """BROKEN SEARCH PAGE - INSIDE HOME PAGE"""
    """last page navigation is broken in Docker website"""
    """This scenario enters a keyword into the search bar and clicks on the last page of search results."""
    """The functionality is broken at this point of time"""
    """1. Nothing is displayed on the page - This scenario is tested here. I have asserted that search results should 
    be present, hence the assertion fails in this case. """
    """2. If the same search is performed again, by clicking enter, search results appear but no pages/pagination"""

    def test_navigate_to_last_page(self):
        self.main_page = MainPage(self.driver)
        signin_page = self.main_page.click_signin_button()
        home_page = signin_page.do_login(TestData.DOCKER_ID, TestData.PASSWORD)
        home_page.search_with_keyword(TestData.SEARCH_CRITERIA_1)
        broken_page = home_page.check_last_page_validity()
        assert broken_page is False

    """NEGATIVE TEST CASE"""
    """Testing for session management once the user is logged out by clicking the back button on browser"""
    """Asserting the value of docker_id if present on the page after logout"""

    def test_back_button_after_logout(self):
        self.main_page = MainPage(self.driver)
        signin_page = self.main_page.click_signin_button()
        home_page = signin_page.do_login(TestData.DOCKER_ID, TestData.PASSWORD)
        home_page.click_fingerprint_image()
        home_page.click_logout()
        check = home_page.check_back_button()
        assert check

    # def test_homepage_title(self):
    #     self.main_page = MainPage(self.driver)
    #     signin_page = self.main_page.click_signin_button()
    #     home_page = signin_page.do_login(TestData.DOCKER_ID, TestData.PASSWORD)
    #     home_title = home_page.verify_page_title(TestData.HOME_PAGE_TITLE)
    #     assert home_title == TestData.HOME_PAGE_TITLE

    # def test_username(self):
    #     self.main_page = MainPage(self.driver)
    #     signin_page = self.main_page.click_signin_button()
    #     home_page = signin_page.do_login(TestData.DOCKER_ID, TestData.PASSWORD)
    #     docker_id = home_page.get_username()
    #     assert docker_id == TestData.DOCKER_ID