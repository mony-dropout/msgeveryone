from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
service = Service('/usr/local/bin/chromedriver')  # Adjust path if needed
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")
time.sleep(45)  # Allow time for manual login if needed

try:
    # Step 1: Click the Search Button
    search_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Search or start new chat"]')
    search_button.click()
    print("Search button clicked!")

    # Step 2: Type into Search Field
    # Try each method to target the search field; uncomment one at a time if needed:
    search_input = driver.find_element(By.CSS_SELECTOR, '[aria-label="Search or start new chat"]')
    search_input.send_keys("Test Contact Name")  # Type a sample name
    search_input.send_keys(Keys.ENTER)  # Simulate hitting "Enter" key
    print("Search input completed!")

    time.sleep(5)  # Pause to observe behavior
finally:
    driver.quit()




