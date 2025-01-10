from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Open Chrome and go to the website
driver = webdriver.Chrome()
driver.get("https://google.com")
time.sleep(3)  # Wait for the page to load

# Step 2: Locate the shadow host element (parent of #shadow-root)
shadow_host = driver.find_element(By.ID, "searchbox")

# Step 3: Use JavaScript to access the shadow root
shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)

# Step 4: Find the element inside the shadow root
search_box = shadow_root.find_element(By.ID, "input")

# Step 5: Interact with the element (type and press Enter)
search_box.send_keys("you can do anything")
search_box.send_keys(Keys.ENTER)
time.sleep(5)

# Step 6: Quit the browser
driver.quit()


