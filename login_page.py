from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):

        self.driver = driver

        # Explicit wait
        self.wait = WebDriverWait(driver, 10)

        # ==================================================
        # LOCATORS
        # ==================================================

        self.username = (
            By.ID,
            "username"
        )

        self.password = (
            By.ID,
            "password"
        )

        self.login_button = (
            By.CSS_SELECTOR,
            "button.radius"
        )

        self.error_message = (
            By.ID,
            "flash"
        )

    # ==================================================
    # ENTER USERNAME
    # ==================================================

    def enter_username(self, username):

        username_field = self.wait.until(
            EC.visibility_of_element_located(
                self.username
            )
        )

        username_field.send_keys(username)

    # ==================================================
    # ENTER PASSWORD
    # ==================================================

    def enter_password(self, password):

        password_field = self.wait.until(
            EC.visibility_of_element_located(
                self.password
            )
        )

        password_field.send_keys(password)

    # ==================================================
    # CLICK LOGIN
    # ==================================================

    def click_login(self):

        login_button = self.wait.until(
            EC.element_to_be_clickable(
                self.login_button
            )
        )

        login_button.click()

    # ==================================================
    # GET ERROR MESSAGE
    # ==================================================

    def get_error_message(self):

        error = self.wait.until(
            EC.visibility_of_element_located(
                self.error_message
            )
        )

        return error.text