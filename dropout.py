from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
# Set path to your Chrome user data
options.add_argument("user-data-dir=/Users/monyatwu/Library/Application Support/Google/Chrome/")
options.add_argument("--profile-directory=Default")  # Adjust if you use a different profile

driver = webdriver.Chrome(options=options)
driver.get("https://google.com")
print(driver.title)

try:
    search_box = driver.find_element(By.CSS_SELECTOR, "textarea#APjFqb")
    search_box.send_keys("ALL THE WAY UP")
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)
finally:
    driver.quit()
