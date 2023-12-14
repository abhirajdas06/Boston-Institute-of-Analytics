import requests

endpoint = "http://127.0.0.1:8000/api/delete/1/"

get_response = requests.delete(endpoint)

print(get_response)