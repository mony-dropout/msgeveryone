#all the way up
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import numpy as np
from selenium.webdriver.support.ui import WebDriverWait

df=pd.read_csv("testing.csv",encoding="utf-8")
df=df.dropna()
df=df.astype(str)

def gen_call(name):
    
    finame=name.split()[0]
    n_l=name.lower()

    if 'sir' in n_l:
        return 'Sir'
    elif 'maam' in n_l:
        return "Ma'am"
    elif 'bhaiya' in n_l:
        return finame+" bhaiya "
    elif 'didi' in n_l:
        return finame+" didi "
    elif 'aunty' in n_l:
        return finame+" aunty "
    elif '98106' in n_l:
        return 'mony'
    else:
        return finame

driver=webdriver.Chrome()
driver.get("https://web.whatsapp.com")
input("press enter after loggin in, hope this works man... just keep going either way")
time.sleep(6)
search_box=driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')

for i,r in df.iterrows():
    if i>0:
        search_box=driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')
    try:
        search_box.clear()
        n=r['name']
        fname=n.split()[0]
        p=r['phone']
        
        search_box.send_keys(f"{p}")
        
        
        contact_box=WebDriverWait(driver,3).until(
            EC.presence_of_element_located((By.XPATH,f"//span[contains(text(), '{fname}') and contains(@title, '{fname}') and @style='min-height: 0px;']"))
        )
        contact_box.click()
        text_box=WebDriverWait(driver,3).until(
            EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p'))
        )
        #string call=what you call them (fname, except if there is bhaiya, didi, maam, aunty, sir)
        call=gen_call(n)
        text_box.send_keys(f"Happy New Year {call} ")
        embut=driver.find_element(By.CSS_SELECTOR,'button[aria-label="Expressions picker"]')
        embut.click()
        happyemo=WebDriverWait(driver,3).until(
        EC.visibility_of_element_located((By.XPATH,"//span[@id='3' and @class='b85 emojik apple']"))
        )
        happyemo.click()
        time.sleep(0.2)
        text_box.send_keys(Keys.RETURN)
        df.loc[i,'sent']=True #is this correct?
    except Exception:
        print("something went wrong")
        continue 
    

df.to_csv("testbillions.csv",index=False)  
time.sleep(6)
driver.quit()      