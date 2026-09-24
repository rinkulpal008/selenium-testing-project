import requests

def test_api_delete():

    url = "https://jsonplaceholder.typicode.com/users/1"


    response = requests.delete(url)


    print("status code", response.status_code)

    print("response",response.text)

    assert response.status_code == 200