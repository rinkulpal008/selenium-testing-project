import requests

def test_api_update():

    url ="https://jsonplaceholder.typicode.com/users/1"


    data_patch = {
        "name":"rinkul pal"
                }

    response = requests.patch(url, json=data_patch)

    data = response.json()

    assert response.status_code ==200

    assert data ["name"] == "rinkul pal"

    