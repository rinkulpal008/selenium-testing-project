import requests


def test_api_headers():

    url = "https://jsonplaceholder.typicode.com/users/1"

    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    print("Status Code:", response.status_code)
    print("Response:", data)
    print("Headers Sent:", headers)

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")