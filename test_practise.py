# def add(a,b):
#     return a+b

# def test_add():
#     assert add(10,10) == 20

# def compare(a,b):
#     return a > b

# def test_comapre():
#     assert compare(10,5)

# def test_string():
#     assert "python".upper() == "PYTHON"


# def test_stringg():
#     assert "RINKUL" == "rinkul"






# def test_login():
#     assert loginPage("rinkul", "1234") == True 


# def test_login1():
#     assert loginPage("", "1234") == False



# def test_login3():
#     assert loginPage("rinkul", "") == False



# def test_login2():
#     assert loginPage("", "") == False


# def loginPage(username , password):
#     if username == "rinkul" and password == "1234":
#         return True 
#     else:
#         return False


# import pytest

# @pytest.mark.parametrize("username,password, expected",[ 
#                          ("rinkul" , "1234" , True),
#                          ("" , "1234" , False),
#                          ("rink" , "12212" , False),
#                          ("" , "" ,  False)
#                             ]
# )

# def test_login(username, password , expected):
#     assert loginPage(username, password) == expected



# import pytest

# @pytest.fixture


# def user():
#     return { "name": "rinkul",
#             "role":"admin"}



# def test_admin(user):
#     assert user["name"] == "rinkul"



# def test_role(user):
#     assert user["role"]== "admin"



# import pytest


# @pytest.fixture

# def database():
#     print("database connected")


#     user_data = { 
#         "name" :"rinkul",
#         "status" :"active"
#     }

#     yield  user_data

#     print("database disconnected")



# def test_page(database):
#     print("test is running")

#     assert database["name"] =="rinkul"
#     assert database["status"]== "active"



# import pytest

# @pytest.fixture

# def database():
#     print ("connected")


#     user_data = {
#         "username": "rinkul",
#         "status" : "middleclass"
#                 }
#     yield user_data
#     print ("database disconnected")


# def test_database1(database):
#       print("test1 is running")
#       assert database["username"]== "rinkul"
#       assert database["status"]== "middleclass"

# def test_database2(database):
#      print("test2 is running")
#      assert database["username"]=="rink"
#      assert database["status"]== "active"

# def test_database3(database):
#       print("test3 is running")
#       assert database["username"]== "rinkul"
#       assert database["password"]== "12312"



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