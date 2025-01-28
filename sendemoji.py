from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pyperclip

driver=webdriver.Chrome()
driver.get("https://web.whatsapp.com")
input("press enter after logging in")
time.sleep(3)
#sb=searchbox
sb=driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')
sb.send_keys("9810695367")
#cn=contactname
cn=WebDriverWait(driver,3).until(
    EC.presence_of_element_located((By.XPATH,"//span[contains(@title,'98106') and contains(text(),'98106') and @style='min-height: 0px;']"))
)
cn.click()
#tb=textbox
tb=WebDriverWait(driver,3).until(
    EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p'))
)
# 😁
#METHOD 1
tb.send_keys("METHOD 1")
try:
    tb.send_keys("😁")
except Exception:
    pass
finally:
    tb.send_keys(Keys.RETURN)
tb=WebDriverWait(driver,3).until(
    EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p'))
)    
#METHOD 2
tb.send_keys("METHOD 2")
try:
    driver.execute_script("arguments[0].innerHTML+='😁';",tb)
except Exception:
    pass
finally:
    tb.send_keys(Keys.RETURN)
tb=WebDriverWait(driver,3).until(
    EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p'))
)
#METHOD 3
tb.send_keys("METHOD 3")
try:
    driver.execute_script("arguments[0].textContent+='😁';",tb)
except Exception:
    pass
finally:
    tb.send_keys(Keys.RETURN)
tb=WebDriverWait(driver,3).until(
    EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p'))
)        
#METHOD 4
tb.send_keys("METHOD 4")
try:
    driver.execute_script("arguments[0].innerText+='😁';",tb)
except Exception:
    pass
finally:
    tb.send_keys(Keys.RETURN)
tb=WebDriverWait(driver,3).until(
    EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p'))
)    
#METHOD 5
tb.send_keys("METHOD 5")
try:
    driver.execute_script("arguments[0].value+='😁';",tb)
except Exception:
    pass
finally:
    tb.send_keys(Keys.RETURN)
tb=WebDriverWait(driver,3).until(
    EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p'))
)    
#METHOD 6
pyperclip.copy("😁")
tb.send_keys("METHOD 6")
try:
    tb.send_keys(Keys.COMMAND+'v')
except Exception:
    pass
finally:
    tb.send_keys(Keys.RETURN)
tb=WebDriverWait(driver,3).until(
    EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p'))
)    
#METHOD 7
tb.send_keys("METHOD 7")
try:
    #this is testing my selenium skills lmao
    embut=driver.find_element(By.CSS_SELECTOR,'button[aria-label="Expressions picker"]')
    embut.click()
    happyemo=WebDriverWait(driver,3).until(
        EC.visibility_of_element_located((By.XPATH,"//span[@id='3' and @class='b85 emojik apple']"))
    )
    happyemo.click()
    time.sleep(0.2)
except Exception:
    pass
finally:
    tb.send_keys(Keys.RETURN)
tb=WebDriverWait(driver,3).until(
    EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p'))
)    
#METHOD 8
tb.send_keys("METHOD 8")
try:
    tb.send_keys("\U0001F601")
except Exception:
    pass
finally:
    tb.send_keys(Keys.RETURN)
    









#how to deal w webdriver exceptions???