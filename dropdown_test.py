from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://automationtesting.co.uk/dropdown.html")     

dropdown = driver.find_element(By.ID, "cars")

select = Select(dropdown)

select.select_by_visible_text("Volkswagen")







next = driver.find_element(By.NAME, "cars")

select_next= Select(next)

select_next.select_by_value("audi")
# select_next.select_by_value("bmw")


if select.first_selected_option.text == "Audi":
    print("✅ Test Passed")
else:
    print("❌ Test Failed")

input("Press Enter to close...")
driver.quit()


