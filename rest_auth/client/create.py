import requests
from getpass import getpass

auth_endpoint = "http://127.0.0.1:8000/api/auth/"

username = input("Enter Username: ")
password = getpass()

auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
token = auth_response.json().get('token', '')

if not token:
    print("Authentication failed.")
else:
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json",
    }


    add_endpoint = "http://127.0.0.1:8000/api/add/"


    data = {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "summary": '''To Kill a Mockingbird is a novel by the American author Harper Lee. 
                    It was published in 1960 and was instantly successful. In the United States, 
                    it is widely read in high schools and middle schools.''',
        "genre": "Fiction",
    }


    post_response = requests.post(add_endpoint, json=data, headers=headers)

    print(post_response.status_code)
    print(post_response.json())
