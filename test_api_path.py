import requests


def test_get_user_by_path():

    # Base API URL
    url = "https://jsonplaceholder.typicode.com/users/1"

    # Send GET request
    response = requests.get(url)

    # Convert response to JSON
    data = response.json()

    # Print response
    print("Status Code:", response.status_code)
    print("Response:", data)

    # Validate status code
    assert response.status_code == 200

    # Validate returned user
    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"
    assert "email" in data