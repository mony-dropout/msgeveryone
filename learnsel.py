from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("file:///Users/monyatwu/Documents/first%20project/testhtml.html")
x=driver.find_element(By.ID,"main-title")
print(x.title)
time.sleep(3)
driver.quit()