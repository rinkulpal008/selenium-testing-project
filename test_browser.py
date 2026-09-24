from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.amazon.in")

# Create wait object
wait = WebDriverWait(driver, 10)

# Wait until search box is visible
search_box = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='twotabsearchtextbox']")
    )
)

search_box.send_keys("Laptop")
search_box.send_keys(Keys.ENTER)

input("Press Enter to close...")
driver.quit()