import requests
import json

#GET
user_input = input("enter id: ")
get_url = f"https://jsonplaceholder.typicode.com/todos/{user_input}"

get_response = requests.get(get_url)
print(get_response.json())

#POST
to_do_item = {"userId": 2, "title": "my to do", "completed": False}
post_url = "https://jsonplaceholder.typicode.com/todos"
#optional header - it works without header as well. to test how it works, you can do the following:
headers = {"Content-Type": "application/json"}
#post_response = requests.post(post_url, json=to_do_item, headers=headers)

#if you need to convert dict into json to send as data
post_response = requests.post(post_url, data=json.dumps(to_do_item), headers=headers)
print(post_response.json())
