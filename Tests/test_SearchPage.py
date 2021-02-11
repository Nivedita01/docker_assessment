from Config.config import TestData
from Pages.MainPage import MainPage
from Tests.test_BasePage import TestBasePage


class TestSearchPage(TestBasePage):

    """BROKEN SEARCH ICON FUNCTIONALITY"""
    """This test validates the search text from main page of the screen."""
    """The user clicks the search icon, enters the keyword and clicks the icon again"""
    """User is redirected to search page but with 'undefined' keyword instead of user's keyword"""
    """This assertion fails since I am asserting user entered keyword with the one on the search page after click on 
    search image """

    def test_search_from_icon_click(self):
        self.main_page = MainPage(self.driver)
        self.main_page.click_search_image()
        search_page = self.main_page.click_search_text(TestData.SEARCH_CRITERIA_2)
        value = search_page.check_search_results_search_image_click()
        assert value == TestData.SEARCH_CRITERIA_2

    # def test_search_bar_overlap(self):
    #     self.main_page = MainPage(self.driver)
    #     self.main_page.click_search_image()
    #     search_page = self.main_page.enter_search_text(TestData.SEARCH_CRITERIA_1)
    #     text = search_page.get_search_criteria_value()
    #     assert text == TestData.SEARCH_BAR
    #
    # def test_overlap(self):
    #     self.main_page = MainPage(self.driver)
    #     self.main_page.click_search_image()
    #     search_page = self.main_page.enter_search_text(TestData.SEARCH_CRITERIA_1)
    #     element = search_page.check_search_criteria_bar()


