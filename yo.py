#do your best every single day
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
driver=webdriver.Chrome()
driver.get("https://web.whatsapp.com")
input("press enter after loggin in")
time.sleep(6)
df=pd.read_csv("testing.csv",encoding="utf-8")
df=df.astype(str)

for i,r in df.iterrows():
    
    n=r['name']
    p=r['phone']
    fname=n.split()[0]
    print(f"trying to message {fname} abhi")
    search_box=driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')
    search_box.clear()
    search_box.send_keys(f"{p}")
    time.sleep(1)
    contact_box=driver.find_element(By.XPATH,f"//span[contains(text(), '{fname}') and contains(@title, '{fname}') and @style='min-height: 0px;']")
    contact_box.click()
    time.sleep(3)
    text_box=driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p')
    text_box.send_keys("happy new year ")
    time.sleep(3)
    embut=driver.find_element(By.CSS_SELECTOR,'button[aria-label="Expressions picker"]')
    embut.click()
    happyemo=WebDriverWait(driver,3).until(
        EC.visibility_of_element_located((By.XPATH,"//span[@id='3' and @class='b85 emojik apple']"))
    )
    happyemo.click()
    time.sleep(0.2) 
    df.loc[i,'sent']=True
df.to_csv("billion.csv",index=False)

    



