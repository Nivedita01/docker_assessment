from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.SearchPage import SearchPage
from Pages.SignInPage import SignInPage


class MainPage(BasePage):

    """By Locators"""
    SEARCH_BUTTON = (By.ID, 'searchToggle')
    SIGNIN_BUTTON = (By.XPATH, "//a[contains(text(), 'Sign In')]")
    SEARCH_IMAGE = (By.CSS_SELECTOR, '#searchToggle')
    SEARCH_TEXT = (By.CSS_SELECTOR, '#searchText')

    """Constructor of Page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.HOME_URL)

    """List of Page Actions for Main Page"""

    """used to click on search image """
    def click_search_image(self):
        if self.is_present(self.SEARCH_IMAGE):
            return self.do_click(self.SEARCH_IMAGE)

    """used to enter values in search box"""
    def enter_search_text(self, search_text):
        if self.is_present(self.SEARCH_TEXT):
            self.do_send_keys_and_enter(self.SEARCH_TEXT, search_text)
            return SearchPage(self.driver)

    """used to send search keyword to search box and clicks on search image"""
    def click_search_text(self, search_text):
        if self.is_present(self.SEARCH_TEXT):
            self.do_send_keys(self.SEARCH_TEXT, search_text)
            self.do_click(self.SEARCH_IMAGE)
            return SearchPage(self.driver)

    """used to check if clicking on Sign In button redirects to Sign In page"""
    def click_signin_button(self):
        self.do_click(self.SIGNIN_BUTTON)
        return SignInPage(self.driver)
