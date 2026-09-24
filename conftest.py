import os
import pytest
from selenium import webdriver


# ==================================================
# PYTEST HOOK
# ==================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)


# ==================================================
# BROWSER FIXTURE
# ==================================================

@pytest.fixture
def driver(request):

    # -------------------------
    # SETUP
    # -------------------------

    driver = webdriver.Chrome()
    driver.maximize_window()

    # Give driver to test
    yield driver

    # -------------------------
    # SCREENSHOT ON FAILURE
    # -------------------------

    if request.node.rep_call.failed:

        # Create screenshots folder
        os.makedirs("screenshots", exist_ok=True)

        # Screenshot name
        screenshot_path = os.path.join(
            "screenshots",
            f"{request.node.name}.png"
        )

        # Take screenshot
        driver.save_screenshot(screenshot_path)

        print(
            f"\nScreenshot saved: {screenshot_path}"
        )

    # -------------------------
    # TEARDOWN
    # -------------------------

    driver.quit()