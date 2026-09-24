from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()



driver.get("https://practice.expandtesting.com/login")

login = driver.find_element(By.ID,'username')
login.send_keys("practise")

password= driver.find_element(By.ID,'password')
password.send_keys('SuperSecretPassword!')


click = driver.find_element(By.XPATH," //*[@id='submit-login']").click()

time.sleep(5)


input("Press Enter to close...")
driver.quit()