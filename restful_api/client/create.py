import requests

endpoint = "http://127.0.0.1:8000/api/add/"
data = {
  
    "title" : "To Kill a Mockingbird",
    "author" : "Harper Lee",
    "summary" : '''To Kill a Mockingbird is a novel by the American author Harper Lee. 
                It was published in 1960 and was instantly successful. In the United States, 
                it is widely read in high schools and middle schools.''',
    "genre" : "Fictoin",
}

get_response = requests.post(endpoint, json=data)

print(get_response)