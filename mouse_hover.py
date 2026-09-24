from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




driver= webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/hovers?utm_source=chatgpt.com")


wait = WebDriverWait(driver, 10)
hoverbtn=driver.find_element(By.XPATH,'//*[@id="content"]/div/div[1]')

actions = ActionChains(driver)

actions.move_to_element(hoverbtn).perform()

time.sleep(10)
driver.quit()
