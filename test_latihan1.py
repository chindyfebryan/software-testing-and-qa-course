import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    # driver.get("https://www.google.com/")
    yield driver
    driver.quit()
    
def test_google_search(browser):
    browser.get("https://www.google.com/")
    search_box = browser.find_element("name", "q")
    search_box.send_keys("Selenium testing" + Keys.RETURN)
    assert "Selenium testing" in browser.title
    
# def test_lain(browser):
#     browser.get("https://www.detik.com/")
#     search_box = browser.find_element("name", + "q")
#     search_box.send_keys("Selenium testing" + Keys.RETURN)
#     assert "Selenium testing" in browser.title