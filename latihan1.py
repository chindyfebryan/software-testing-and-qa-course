from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://pyapp.unhas.ac.id/laboratorium/")
elem = driver.find_element(By.NAME, 'key')
elem.send_keys("rekayasa")
elem.send_keys(Keys.ENTER)
button = driver.find_element(By.ID, 'some_button_id')
button.click()
print("Clicked on button with ID 'some_button_id'")
time.sleep(3600)
driver.close()