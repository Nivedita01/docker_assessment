from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.ForgotPage import ForgotPage
from Pages.HomePage import HomePage
from Pages.SignUpPage import SignUpPage


class SignInPage(BasePage):

    """By Locators"""
    DOCKER_ID = (By.ID, 'nw_username')
    PASSWORD = (By.ID, 'nw_password')
    SIGNIN_BUTTON = (By.ID, 'nw_submit')
    FORGOT_PASSWORD = (By.XPATH, "//a[contains(text(), 'Forgot')]")
    SIGNUP_LINK = (By.XPATH, "//a[contains(text(), 'Sign Up')]")
    INVALID_AUTHENTICATION_MESSAGE = (By.XPATH, "//div[contains(text(), 'Incorrect')]")

    """Constructors of Page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """List of Page Actions for Sign In Page"""

    """used to get login page title"""
    def get_login_page_title(self, title):
        title = self.get_title(title)
        return title

    """used to check if signup link exists"""
    def is_signup_link_exists(self):
        return self.is_visible(self.SIGNUP_LINK)

    """check forgot password link is visible"""
    def is_forgot_link_exists(self):
        return self.is_visible(self.FORGOT_PASSWORD)

    """Verify if a user will be able to login with docker_id and password."""
    def do_login(self, docker_id, password):
        self.do_send_keys(self.DOCKER_ID, docker_id)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.SIGNIN_BUTTON)
        return HomePage(self.driver)

    """Verify if a user will be able to login with invalid docker_id and password."""
    def do_invalid_login(self, docker_id, password):
        self.do_send_keys(self.DOCKER_ID, docker_id)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.SIGNIN_BUTTON)
        return self.get_element_text(self.INVALID_AUTHENTICATION_MESSAGE)

    def click_forgot_link(self):
        self.do_click(self.FORGOT_PASSWORD)
        return ForgotPage(self.driver)

    def click_signup_link(self):
        self.do_click(self.SIGNUP_LINK)
        return SignUpPage(self.driver)
