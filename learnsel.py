#just learn selenium right now
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get("https://google.com")
time.sleep(5)

driver.quit()