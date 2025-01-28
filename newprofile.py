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
phone="9569035187"
search_box=driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')
search_box.send_keys(f"{phone}")
contact


