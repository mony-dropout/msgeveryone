from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pyperclip
import pandas as pd
import numpy as np
options = Options()
options.add_argument('user-data-dir=/Users/monyatwu/selenium_profiles')  # Path to the selenium_profiles directory
options.add_argument('profile-directory=Default')  # Use the Default profile

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(), options=options)
driver.get("https://web.whatsapp.com")
input("press enter when you ready to start bro")
time.sleep(3)
df=pd.read_csv("testing.csv")
df=df.astype(str)
df['sent']=0
pyperclip.copy("😁")
for i, r in df.iterrows():
    try: 
        fullname=r['name']
        phonenum=r['phone']
        firstname=fullname.split()[0]
        
        

        search_box=driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')
        search_box.clear()
        search_box.send_keys(f"{phonenum}")
        

        time.sleep(1)
        WebDriverWait(driver,3).until(
            EC.presence_of_element_located((By.XPATH,f"//span[contains(text(),'{firstname}') and contains(@title,'{firstname}') and @style='min-height: 0px;']"))
        )
        #contact=driver.find_elements(By.XPATH, f"//span[contains(text(), '{firstname}') and contains(@title, '{firstname}') and @style='min-height: 0px;']")
        contact = driver.find_elements(By.XPATH,f"//span[contains(text(),'{firstname}') and contains(@title,'{firstname}') and @style='min-height: 0px;']")
        contact[0].click()  # Always click the first matching result

        #contact[0].click()
        text_box=WebDriverWait(driver,3).until(
            EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p'))
        )
        if firstname=="98106":
            firstname="mony"
        text_box.send_keys(f"Happy New Year {firstname}")
        text_box.send_keys(Keys.COMMAND + 'v')
        embut=driver.find_element(By.CSS_SELECTOR,'button[aria-label="Expressions picker"]')
        embut.click()
        happyemo=WebDriverWait(driver,3).until(
            EC.visibility_of_element_located((By.XPATH,"//span[@id='3' and @class='b85 emojik apple']"))
        )
        happyemo.click()
        time.sleep(1)
        df.loc[i,"sent"]=1
        text_box.send_keys(Keys.RETURN)
        
        search_box.clear()
        
        time.sleep(1)
    except Exception:
        print(f"{firstname} couldnt work damn")
        
        search_box=driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')
        
        driver.execute_script("arguments[0].value = '';", search_box)  # Clear search box forcefully
        search_box.send_keys(Keys.BACKSPACE * 13)  # Extra backup

        continue
    
df.to_csv("keepgoingbruh1.csv")
time.sleep(6)
driver.quit()
    