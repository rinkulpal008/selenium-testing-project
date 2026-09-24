from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver =webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/context_menu?utm_source=chatgpt.com")
wait = WebDriverWait(driver, 10)


right_click = driver.find_element(By.ID,"hot-spot")



actions = ActionChains(driver)

actions.context_click(right_click).perform()

my=driver.switch_to.alert

print(my.text)

my.accept()



time.sleep(6)
driver.quit()