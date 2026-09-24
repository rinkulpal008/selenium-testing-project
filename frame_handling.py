from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/nested_frames?utm_source=chatgpt.com")

driver.switch_to.frame("frame-top")

driver.switch_to.frame("frame-left")

text = driver.find_element(By.TAG_NAME,"body").text
print(text)


time.sleep(4)
driver.quit()
