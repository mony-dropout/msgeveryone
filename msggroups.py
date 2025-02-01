#//*[@id="pane-side"]/div[1]/div/div/div[1]
#//*[@id="pane-side"]/div[1]/div/div/div[2]
#ara poker(3): //*[@id="pane-side"]/div[1]/div/div/div[3]/div/div/div/div[2]/div[1]/div[1]/span OR 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import pyperclip
import pandas as pd
import numpy as np
options=Options()
options.add_argument("user-data-dir=/Users/monyatwu/selenium_profiles")
options.add_argument("profile-directory=Default")

driver=webdriver.Chrome(service=Service(), options=options)
driver.get("https://web.whatsapp.com")
input("press enter when youre ready to keep going ;)")
time.sleep(6)
groups_button=driver.find_element(By.XPATH,'//*[@id="group-filter"]/div/div')
groups_button.click()
time.sleep(1)
inside_view=driver.find_element(By.XPATH,'//*[@id="pane-side"]/div[1]/div/div/div[1]')
inside_view.click()
time.sleep(6)
outside_view=driver.find_element(By.XPATH,'//*[@id="pane-side"]/div[1]/div/div/div[10]')
outside_view.click()
input("press enter if you clicked on it lol")
driver.quit()