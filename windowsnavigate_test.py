from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/windows")

# Get parent window
parent_Window = driver.current_window_handle

print("Parent Window:")
print(parent_Window)

# Open new window
driver.find_element(By.XPATH, "//*[@id='content']/div/a").click()

time.sleep(2)

# Get all windows
all_windows = driver.window_handles

print("All Windows:")
print(all_windows)
driver.switch_to.window(parent_Window)



# Print current page title
print("Current Title:", driver.title)

# Count windows
num_tab = len(driver.window_handles)

print("Number of Tabs:", num_tab)

time.sleep(5)

driver.quit()