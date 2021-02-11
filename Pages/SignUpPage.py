from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class SignUpPage(BasePage):

    """By Locators"""
    DOCKER_ID = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    SIGNIN_BUTTON = (By.ID, 'submit')
    EMAIL = (By.ID, 'email')
    SIGNIN_LINK = (By.XPATH, "//a[contains(text(), 'Sign In')]")

    """Constructors of Page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """List of Page Actions for SignUp Page"""

    """copies password value and pastes to email field"""
    def copy_password_text(self, password):
        self.do_send_keys(self.PASSWORD, password)
        self.element_double_click(self.PASSWORD)
        self.copy_element_value(self.PASSWORD)
        self.paste_element_value(self.EMAIL)
        pasted_text = self.get_element_text(self.EMAIL)
        return pasted_text


    def enter_invalid_dockerid(self, docker_id):
        self.do_send_keys(self.DOCKER_ID, docker_id)

    def enter_invalid_emailid(self, email_id):
        self.do_send_keys(self.EMAIL, email_id)

    def enter_invalid_password(self, password):
        self.do_send_keys(self.PASSWORD, password)

    def enter_valid_dockerid(self, docker_id):
        self.do_send_keys_and_tab(self.DOCKER_ID, docker_id)

    def enter_valid_emailid(self, email_id):
        self.do_send_keys_and_tab(self.EMAIL, email_id)

    def enter_valid_password(self, password):
        self.do_send_keys_and_tab(self.PASSWORD, password)


