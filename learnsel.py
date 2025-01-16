from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
input("press enter after logging in")
time.sleep(3)

# Message 1
search_box = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')
search_box.send_keys("8375096016")  # Replace with the first contact's name/number
input("press enter if you searched correctly")
time.sleep(3)
contact_box = driver.find_elements(By.XPATH, "//span[contains(text(), 'Mummy') and contains(@title, 'Mummy') and @style='min-height: 0px;']")
contact_box[0].click()
input("press enter if you clicked on contact")
time.sleep(3)
text_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p')
text_box.send_keys("guess how i sent this message ;) im going to achieve all my dreams, this is sooo fun ;)")
time.sleep(2)
text_box.send_keys(Keys.RETURN)
input("press enter if you sent message")
time.sleep(2)

# Clear search box for next contact
search_box = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')
search_box.clear()

# Message 2
search_box.send_keys("9810695367")  # Replace with the second contact's name/number
input("press enter if you searched correctly")
time.sleep(3)
contact_box = driver.find_elements(By.XPATH,"//span[contains(text(), '98106') and contains(@title, '98106') and @style='min-height: 0px;']")
contact_box[0].click()
input("press enter if you clicked on contact")
time.sleep(3)
text_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p')
text_box.send_keys("guess how i sent this message ;) im going to achieve all my dreams, this is sooo fun ;)")
time.sleep(2)
text_box.send_keys(Keys.RETURN)
input("press enter if you sent message")
time.sleep(2)

input("press enter if you'll keep working hard")
