from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Path to your chromedriver (replace with your path if needed)
service = Service("/usr/local/bin/chromedriver")

# Start the Chrome browser
driver = webdriver.Chrome(service=service)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for the page to load
print("WhatsApp Web opened. Scan the QR code if not already logged in.")
time.sleep(10)  # Adjust this if needed
