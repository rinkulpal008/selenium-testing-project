from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
# Launch Chrome


driver = webdriver.Chrome()

# Open website

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")

wait = WebDriverWait(driver, 10)




# Click the first checkbox
check_box = driver.find_element(By.XPATH, "//*[@id='checkboxes']/input[1]")
check_box.click()





print("Checkbox 1:", "Passed ✅"if check_box.is_selected() else "Failed ❌")
# print("Checkbox 2:", "Passed ✅" if checkbox2.is_selected() else "Failed ❌")

# Pause so you can see the result
input("Press Enter to close...")

# Close browser
driver.quit()