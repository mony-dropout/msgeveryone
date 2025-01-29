#do your best every single day
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('user-data-dir=/Users/monyatwu/selenium_profiles')  # Path to the selenium_profiles directory
options.add_argument('profile-directory=Default')  # Use the Default profile

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(), options=options)

driver.get("https://web.whatsapp.com")
input("press enter after loggin in")
time.sleep(6)
phonenum="9810695367"
firstname="98106"
search_box = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')
search_box.clear()
search_box.send_keys(f"{phonenum}")

time.sleep(1)  # Allow search box to populate

contact = driver.find_elements(By.XPATH, f"//span[contains(text(), '{firstname}') and contains(@title, '{firstname}') and @style='min-height: 0px;']")

contact[0].click()
            
text_box = WebDriverWait(driver, 3).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p'))
)
text_box.send_keys(f"Living my dream {firstname}")
text_box.send_keys(Keys.COMMAND + 'v')

embut = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Expressions picker"]')
embut.click()
happyemo = WebDriverWait(driver, 3).until(
    EC.visibility_of_element_located((By.XPATH, "//span[@id='3' and @class='b85 emojik apple']"))
)
happyemo.click()
time.sleep(0.2)

text_box.send_keys(Keys.RETURN)
search_box.clear()

time.sleep(6)
driver.quit()