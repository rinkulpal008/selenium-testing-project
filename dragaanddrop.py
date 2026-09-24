from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/drag_and_drop?utm_source=chatgpt.com")


source = driver.find_element(By.ID,"column-a")
target = driver.find_element(By.ID,"column-b")

actions =ActionChains(driver)

actions.drag_and_drop(source,target).perform()

time.sleep(5)
driver.quit()
