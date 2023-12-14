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

    delete_endpoint = "http://127.0.0.1:8000/api/delete/1/"

    delete_response = requests.delete(delete_endpoint, headers=headers)

    print(delete_response.status_code)

