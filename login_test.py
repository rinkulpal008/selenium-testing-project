import pytest

from pages.login_page import LoginPage


# ==================================================
# SMOKE TEST
# ==================================================

@pytest.mark.smoke
def test_valid_login(driver):

    # Open login page
    driver.get(
        "https://the-internet.herokuapp.com/login"
    )

    # Create Page Object
    login_page = LoginPage(driver)

    # Enter username
    login_page.enter_username(
        "tomsmith"
    )

    # Enter password
    login_page.enter_password(
        "SuperSecretPassword!"
    )

    # Click login
    login_page.click_login()

    # Verify successful login
    assert "/secure" in driver.current_url


# ==================================================
# REGRESSION TEST
# ==================================================

@pytest.mark.regression
def test_login_page_title(driver):

    # Open login page
    driver.get(
        "https://the-internet.herokuapp.com/login"
    )

    # Verify title
    assert "The Internet" in driver.title


# ==================================================
# REGRESSION TEST
# ==================================================

@pytest.mark.regression
def test_login_page_url(driver):

    # Open login page
    driver.get(
        "https://the-internet.herokuapp.com/login"
    )

    # Verify URL
    assert "/login" in driver.current_url


# ==================================================
# NEGATIVE LOGIN TEST
# ==================================================

@pytest.mark.regression
def test_invalid_login(driver):

    # Open login page
    driver.get(
        "https://the-internet.herokuapp.com/login"
    )

    # Create Page Object
    login_page = LoginPage(driver)

    # Enter valid username
    login_page.enter_username(
        "tomsmith"
    )

    # Enter incorrect password
    login_page.enter_password(
        "WrongPassword"
    )

    # Click login
    login_page.click_login()

    # Get error message
    error_message = login_page.get_error_message()

    # Verify error
    assert "Your password is invalid!" in error_message