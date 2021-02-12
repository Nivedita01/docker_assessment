import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Config.config import TestData

"""For parallel execution on multiple browsers"""
# @pytest.fixture(params=["chrome", "firefox"], scope="class")

"""Considering single browser for execution in this demo"""


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = web_driver
    yield
    web_driver.close()
