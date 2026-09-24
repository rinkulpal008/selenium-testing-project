import requests


def test_send_data():


    url = "https://jsonplaceholder.typicode.com/users"


    send_data = {
        "name": "rinkul",
        "email":"rinkulp12@gmail.com"
    }

    response= requests.post(url,json=send_data)

    data =response.json()


    print('status code',response.status_code)
    print('response',data)


    assert response.status_code == 201

    assert data["name"] == "rinkul" 
    assert data["email"] =="rinkulp12@gmail.com"