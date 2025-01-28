#all the way up
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import numpy as np
from selenium.webdriver.support.ui import WebDriverWait

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

driver=webdriver.Chrome()
driver.get("https://web.whatsapp.com")
input("press enter after loggin in, hope this works man... just keep going either way")
time.sleep(6)
#search_box=driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')
#im keeping this outside cos htis locationn never changes, so we dont need to search for it again and again
#basic thing is if n=name string, p=phone (we'll get from loop)
#remember to clear search box at end of this shi
#add a try statement to all of this, finally clear search box tho
for i, r in df.iterrows():
    search_box=driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')
    try:

        n=r['name']
        p=r['phone']
        
        search_box.send_keys(f"{p}") 
        
        fname=n.split()[0]
        contact_box=WebDriverWait(driver,3).until(
            EC.presence_of_element_located(By.XPATH,f"//span[contains(text(), '{fname}') and contains(@title, '{fname}') and @style='min-height: 0px;']")
        )
        contact_box.click()
        text_box=WebDriverWait(driver,3).until(
            EC.visibility_of_element_located(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p')
        )
        #string call=what you call them (fname, except if there is bhaiya, didi, maam, aunty, sir)
        call=gen_call(n)
        text_box.send_keys(f"Happy New Year '{call}'")
        driver.execute_script("arguments[0].innerHTML=arguments[0].innerHTML+'😁😁😁';",text_box)
        text_box.send_keys(Keys.RETURN)
        df.loc[i,'sent']=True #is this correct?
    except Exception:
        continue 
    finally:
        search_box.clear()
df.to_csv("billion.csv",index=False)








