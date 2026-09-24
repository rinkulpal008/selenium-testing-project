import requests

def test_api_update():


    url = "https://jsonplaceholder.typicode.com/users/1"

    data_update = {

        "name": "RINKUL21",
        "email": 'rinkulpal1@gmail.com'
    }

    response = requests.put(url,json=data_update)


    data =response.json()

    print("status code", response.status_code)
    print("response",data)

    assert response.status_code == 200

    assert data ["name"] =="RINKUL21"
    assert data ["email"] == "rinkulpal1@gmail.com"