from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.google.com")
print("page title is", driver.title)
driver.quit()

