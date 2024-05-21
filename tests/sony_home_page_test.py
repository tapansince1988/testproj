from conftest import *

def home_page_title_test(driver):
    page_title = driver.title
    expected_page_title = 'Sony India | Latest Technology News | Electronics | Entertainment'
    assert page_title == expected_page_title

