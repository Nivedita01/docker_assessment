from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This class is the parent of all pages"""

"""It contains all generic methods and utilities for all pages"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def do_send_keys_and_enter(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text,
                                                                                                     Keys.ENTER)

    def do_send_keys_and_tab(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text,
                                                                                                     Keys.TAB)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
        return element

    def get_element_value(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).get_attribute(
            'value')
        return element

    def copy_element_value(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.CONTROL, "c")

    def paste_element_value(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.CONTROL, "v")

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def is_present(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        return bool(element)

    def is_not_present(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(by_locator))
        return bool(element)

    def element_double_click(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        # create action chain object
        action = ActionChains(self.driver)
        # double click the item
        action.double_click(on_element=element)
        # perform the operation
        action.perform()
