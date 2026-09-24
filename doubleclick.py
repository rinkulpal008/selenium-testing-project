from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver= webdriver.Chrome()

driver.get("https://www.qafeast.com/demo?utm_source=chatgpt.com")

single_click=driver.find_element(By.XPATH,'//*[@id="block-one"]/div/div/div[1]/div/ul/li[10]/label')

action= ActionChains(driver)

action.double_click(single_click).perform()

doubl_click=driver.find_element(By.XPATH,'//*[@id="rghtsideinnerbox_10"]/div/p')

action.double_click(doubl_click).perform()


time.sleep(10)
driver.quit()
