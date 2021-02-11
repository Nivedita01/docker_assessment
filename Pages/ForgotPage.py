from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class ForgotPage(BasePage):

    """Locators"""

    ENTER_EMAIL_ADDRESS = (By.XPATH, "//div[contains(text(), 'Enter')]")
    SEND_BUTTON = (By.XPATH, "//button[contains(text(), 'Send')]")
    SIGN_IN_BUTTON = (By.XPATH, "//a[contains(text(), 'Sign In')]")
    CHECK_MESSAGE = (By.XPATH, "//div[contains(text(), 'Check')]")
    INVALID_EMAIL = (By.XPATH, "//div[contains(text(), 'Invalid')]")

    """Constructors of Page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """List of Page Actions for Forgot Page"""

    """checks if send button is present on the page and clicks on it"""
    def is_send_button_present(self):
        if self.is_present(self.SEND_BUTTON):
            self.do_click(self.SEND_BUTTON)

    """checks if sign in button is present on the page and clicks it"""
    def is_signin_button_present(self):
        if self.is_present(self.SIGN_IN_BUTTON):
            self.do_click(self.SIGN_IN_BUTTON)

    def enter_email_id_click(self, email):
        self.do_send_keys(self.ENTER_EMAIL_ADDRESS, email)
        return self.get_element_text(self.CHECK_MESSAGE)

    def enter_email_id_enter(self, email):
        self.do_send_keys(self.ENTER_EMAIL_ADDRESS, email)
        return self.get_element_text(self.CHECK_MESSAGE)

    """clicks on send button and gets the value of text on email address field"""
    def click_send_no_email(self):
        self.do_click(self.SEND_BUTTON)
        return self.get_element_text(self.INVALID_EMAIL)

