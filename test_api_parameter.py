import requests


def test_api_param():


    url = "https://jsonplaceholder.typicode.com/users"

    param = {
        "id": 1
    }

    response = requests.get(url, params=param)

    data = response.json()


    print("status code", response.status_code)
    print("response",data)

    assert response.status_code == 200

    assert len(data) > 0
    assert data[0]["id"] ==1
