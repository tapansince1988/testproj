import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

BaseURL = 'https://www.sony.co.in/'
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    # driver.get(BaseURL)
    yield driver
    driver.quit()
