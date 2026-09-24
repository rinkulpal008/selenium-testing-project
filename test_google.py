# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()

# driver.get("https://www.amazon.in")

# time.sleep(5)   # Give the page time to load

# search = driver.find_element(By.ID, "twotabsearchtextbox")

# search.send_keys("iphone 16")


# search_button = driver.find_element(By.ID, "nav-search-submit-button")
# search_button.click()

# driver.implicitly_wait(10)


# print(driver.title)

# driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://www.amazon.in")

wait = WebDriverWait(driver, 10)

search = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#twotabsearchtextbox"))
)

search.click()



# search_button = driver.find_element(By.ID, "nav-search-submit-button")
# search_button.click()


time.sleep(4)