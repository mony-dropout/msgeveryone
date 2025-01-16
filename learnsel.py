from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://web.whatsapp.com")
input("press enter after logging in")
time.sleep(3)
search_box=driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')
search_box.send_keys("7003554510")
input("press enter if you searched correctly")
time.sleep(3)
contact_box=driver.find_elements(By.XPATH,"//span[contains(text(), 'Sagnik') and contains(@title, 'Sagnik') and @style='min-height: 0px;']")
contact_box[0].click()
input("press enter if you clicked on contact")
time.sleep(3)
text_box=driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p')    
text_box.send_keys("guess how i sent this message ;) we can do anything bruh")
time.sleep(2)
text_box.send_keys(Keys.RETURN)
input("press enter if you sent messaage")
time.sleep(2)
input("press enter if youll keep working hard")