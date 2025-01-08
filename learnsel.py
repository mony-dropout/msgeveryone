from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Step 2: Open the HTML file
    driver.get("file:///Users/monyatwu/Documents/first%20project/testhtml.html")
    time.sleep(2)  # Wait for the page to load

    # Step 3: Locate the Shadow Host
    shadow_host = driver.find_element(By.ID, "shadow-host")

    # Step 4: Access the Shadow Root
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)

    # Step 5: Find elements inside the Shadow DOM
    shadow_paragraph = shadow_root.find_element(By.CSS_SELECTOR, "p")
    shadow_button = shadow_root.find_element(By.CSS_SELECTOR, "#shadow-button")

    # Step 6: Print text from Shadow DOM elements
    print("Text inside shadow paragraph:", shadow_paragraph.text)

    # Step 7: Interact with Shadow DOM elements
    shadow_button.click()
    print("Shadow button clicked!")

    time.sleep(2)  # Observe the interaction
finally:
    # Step 8: Close the browser
    driver.quit()
