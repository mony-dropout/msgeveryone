from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
import time
driver=webdriver.Chrome()
driver.get("https://www.instagram.com/p/DAi7hSDgacV/?hl=en&img_index=5")
time.sleep(12)
driver.quit()