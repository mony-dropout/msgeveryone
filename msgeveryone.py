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

df=pd.read_csv("bestever.csv",encoding="utf-8")
df=df.dropna()
df=df.astype(str)

def gen_call(name):
    n_l=name.lower()
    fname=name.split()[0]

    if 'sir' in n_l:
        return 'Sir'
    elif 'maam' in n_l:
        return "Ma'am"
    elif 'bhaiya' in n_l:
        return fname+" bhaiya "
    elif 'didi' in n_l:
        return fname+" didi "
    elif 'aunty' in n_l:
        return fname+" aunty "
    else:
        return fname


input("press enter when you ready to start bro")
time.sleep(3)

df['sent']=0
pyperclip.copy("😁")
for i, r in df.iterrows():
    try: 
        fullname=r['name']
        phonenum=r['phone']
        firstname=fullname.split()[0]
        call=gen_call(fullname)
        

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
            call="Mony"
        if phonenum=="9569035187":
            call="Kuku"
        text_box.send_keys(f"Happy New Year {call}")
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
        search_box.send_keys(Keys.BACKSPACE * 19)  # Extra backup

        continue
input("you did it bruh, for real")   
df.to_csv("atwu.csv")
time.sleep(6)
driver.quit()

#we can do anything mony, this was our first ever project
#this is just the start of a wonderful journey bruh, you can do anything
#just enjoy life and every single day just do your best, just work as hard as possible every single day, just get better every single day, that is it
#have fun and remember that youre living your dream ;)
#all the way up








