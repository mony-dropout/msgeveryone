from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://web.whatsapp.com")
input("press enter after logging in")
search_box=driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')
search_box.send_keys("9810695367")
time.sleep(2)
contact_box=driver.find_element(By.CSS_SELECTOR,"span.x1iyjqo2.x6ikm8r.x10wlt62.x1n2onr6.xlyipyv.xuxw1ft.x1rg5ohu._ao3e")
contact_box.click()
time.sleep(2)
