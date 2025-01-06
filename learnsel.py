from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("file:///Users/monyatwu/Documents/first%20project/learnhtml.html")
time.sleep(6)
driver.quit()
