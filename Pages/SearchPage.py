from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class SearchPage(BasePage):

    """By Locators"""
    SEARCH_BOX = (By.ID, 'edit-keys')
    SEARCH_BUTTON = (By.ID, 'edit-submit')
    SEARCH_TITLE = (By.CSS_SELECTOR, 'h1.title')
    SEARCH_TEXT = (By.ID, 'edit-keys')

    """Constructors of Page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions for Search Page"""

    def get_search_criteria_value(self):
        if self.is_present(self.SEARCH_TITLE):
            return self.get_element_text(self.SEARCH_TITLE)

    def check_search_criteria_bar(self):
        if self.is_present(self.SEARCH_TITLE):
            self.element_double_click(self.SEARCH_TITLE)

    def check_search_results_search_image_click(self):
        return self.get_element_value(self.SEARCH_TEXT)
