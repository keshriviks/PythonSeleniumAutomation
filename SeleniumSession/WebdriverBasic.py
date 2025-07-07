from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.NAME,'q').send_keys("Vikash Keshri")
print(driver.title)

#driver.quit()