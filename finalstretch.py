from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas
import numpy as np
import pyperclip


# Define ChromeOptions
options = Options()
options.add_argument('user-data-dir=/Users/monyatwu/selenium_profiles')  # Path to the selenium_profiles directory
options.add_argument('profile-directory=Default')  # Use the Default profile

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(), options=options)

# Test the profile
driver.get("https://web.whatsapp.com")
input("press enter when you're ready")
time.sleep(6)
#########################################################################################################################
fullname="Mony Kuku Number"
firstname=fullname.split()[0]
secondname=fullname.split()[1]
phone="9569035187"
pyperclip.copy("😈")
search_box=driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')
search_box.send_keys(f"{phone}")


contact=driver.find_elements(By.XPATH, f"//span[contains(text(), '{firstname}') and contains(@title, '{firstname}') and @style='min-height: 0px;']")
contact[0].click()
text_box=WebDriverWait(driver,3).until(
    EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p'))
)
text_box.send_keys(f"we can do anything {secondname}, work, just work, make the little kid with big dreams proud ")
text_box.send_keys(Keys.COMMAND+'v')
text_box.send_keys(Keys.RETURN)

print("keep going, this is what you chose")
time.sleep(6)
driver.quit()    



