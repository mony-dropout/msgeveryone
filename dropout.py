from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://web.whatsapp.com")
time.sleep(10)
print(driver.title)
driver.quit()