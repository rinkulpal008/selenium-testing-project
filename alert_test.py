from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/alerts.html")

driver.find_element(By.ID, "empty-alert").click()

alert = driver.switch_to.alert

print(alert.text)




alert.accept()

time.sleep(5)

print("✅ Alert Accepted Successfully")

input("Press Enter to close...")
driver.quit()