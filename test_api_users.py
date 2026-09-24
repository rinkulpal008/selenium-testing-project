import requests


def test_get_user():

    url = "https://jsonplaceholder.typicode.com/users/1"

    response = requests.get(url)

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200