from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up ChromeDriver
driver=webdriver.Chrome()

# Open Google
driver.get("https://google.com")

# Find the search bar and type
search_bar = driver.find_element(By.NAME, "q")  # Google search bar uses name="q"
search_bar.send_keys("Hello World")  # Type the query
search_bar.send_keys(Keys.RETURN)  # Press Enter

# Wait and quit
time.sleep(5)
driver.quit()


