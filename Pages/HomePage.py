from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):

    """Locators"""

    DOCKER_ID = (By.CSS_SELECTOR, 'button[data-testid = navBarUsernameDropdown]')
    FINGERPRINT_IMAGE = (By.CSS_SELECTOR, 'img[data-testid = imgSource]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, 'li#logoutButton')
    SEARCH_BOX = (By.CSS_SELECTOR, 'input[data-testid = autocompleteInput]')
    FILTER_BOX = (By.ID, 'imageFilterList')
    PAGINATION_LAST = (By.CSS_SELECTOR, 'li[data-testid = pagination-last]')
    SEARCH_RESULT = (By.CSS_SELECTOR, 'a[data-testid = imageSearchResult]')

    """Constructor of Page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """List of Page Actions for Home Page"""

    def verify_page_title(self, title):
        return self.get_title(title)

    def get_username(self):
        return self.get_element_text(self.DOCKER_ID)

    """clicks on the fingerprint image, user details button if it is visible"""
    def click_fingerprint_image(self):
        if self.is_visible(self.FINGERPRINT_IMAGE):
            return self.do_click(self.FINGERPRINT_IMAGE)

    """clicks on Logout button if visible"""
    def click_logout(self):
        if self.is_visible(self.LOGOUT_BUTTON):
            return self.do_click(self.LOGOUT_BUTTON)

    """checks back button functionality after logout"""
    def check_back_button(self):
        self.driver.execute_script("window.history.go(-1)")
        return self.is_not_present(self.DOCKER_ID)

    """keyword is entered and checks if there is a filter box on the left pane"""
    def search_with_keyword(self, keyword):
        self.do_send_keys_and_enter(self.SEARCH_BOX, keyword)
        return self.is_present(self.FILTER_BOX)

    """last button on pagination is clicked and search result is verified."""
    def check_last_page_validity(self):
        self.do_click(self.PAGINATION_LAST)
        return self.is_not_present(self.SEARCH_RESULT)