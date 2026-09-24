import pytest

@pytest.fixture(scope="module")
def laptop():
    print("\nLaptop Started")
    yield
    print("\nLaptop Shutdown")


def test_chrome(laptop):
    print("Chrome Opened")


def test_vscode(laptop):
    print("VS Code Opened")


def test_terminal(laptop):
    print("Terminal Opened")