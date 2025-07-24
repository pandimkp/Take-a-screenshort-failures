from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

driver: WebDriver = webdriver.Chrome()
driver.get("https://amazon.in")

try:
    assert 'Not Present' in driver.title
except AssertionError:  # 1. Exception name should not be in quotes
    driver.save_screenshot("failure.png")
    print("Screenshot captured on failure")  # 2. Moved inside the except block
finally:  # 3. Added finally block for proper cleanup
    driver.quit()
