from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Path to your Chrome profile
profile_path = "/Users/monyatwu/Library/Application Support/Google/Chrome/Default"

# Setting up Chrome options
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={profile_path}")  # Use your Chrome profile
options.add_argument("--start-maximized")  # Start Chrome maximized
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  # Exact Chrome executable path

# Launch Chrome with WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")
print("Page title is:", driver.title)

# Keep the browser open for manual interaction
# You can adjust the sleep duration

time.sleep(100)
driver.quit



