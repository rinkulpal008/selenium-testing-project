from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get("https://demoqa.com/radio-button")


radio_btn= driver.find_element(By.XPATH, "//*[@id='impressiveRadio']")
radio_btn.click()


print(radio_btn.is_selected())

if radio_btn.is_selected():
    print("test is passed")

else:
    print("test is failed")



input("Press Enter to close...")

driver.quit()


