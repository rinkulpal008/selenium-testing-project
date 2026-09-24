import requests


def test_get_user():

    url = "https://jsonplaceholder.typicode.com/users/1"

    response = requests.get(url)

    data = response.json()

    print("Status Code:", response.status_code)
    print("Response:", data)

    assert response.status_code == 200
    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"
    assert "email" in data

    assert data["address"]["city"] == "Gwenborough"
    assert data["company"]["name"] == "Romaguera-Crona"