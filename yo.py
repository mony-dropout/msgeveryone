from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("file:///Users/monyatwu/Documents/first%20project/kd.html")
emoji=driver.find_element(By.ID, "goals")
but=driver.find_element(By.XPATH,'/html/body/button')
but.click()
emoji.send_keys("Keep working mony \U0001F60A")
time.sleep(10)
driver.quit()
