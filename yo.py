from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
print(driver.title)

# Wait for user to log in
input("Press Enter once you've logged in.")

# Step 1: Search for the contact
search_box = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='side']/div[1]/div/div[2]/div[2]/div/div/p"))
)
search_box.send_keys("9810695367")  # Replace with your contact
time.sleep(3)

# Step 2: Click on the contact
contact = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='pane-side']//span[contains(text(), '9810695367')]"))
)
contact.click()

# Step 3: Wait for the message input box
message_box = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='conversation-compose-box-input']"))
)

# Ensure the element is visible and enabled
driver.execute_script("arguments[0].scrollIntoView(true);", message_box)  # Scroll to the element
time.sleep(1)  # Give time for scrolling (if needed)
message_box.click()  # Focus on the input box

# Step 4: Send the message
message_box.send_keys("Just keep going!")  # Replace with your message
message_box.send_keys(Keys.RETURN)

# Keep the browser open for debugging
input("Press Enter to close.")
driver.quit()
