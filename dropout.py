from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://google.com")
print(driver.title)

x=driver.find_element(By.ID,"APjFqb")
x.send_keys("mony")
time.sleep(0.5)
driver.execute_script("arguments[0].value=arguments[0].value+ 'All the way up 😈' ;",x)
x.send_keys(Keys.RETURN)
input("hi")
driver.quit()