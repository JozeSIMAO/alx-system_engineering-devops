#!/usr/bin/python3
"""Dictionary of list of dictionaries"""

import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    users_response = requests.get(f"{base_url}/users")
    todos_response = requests.get(f"{base_url}/todos")

    users_data = users_response.json()
    todos_data = todos_response.json()

    todo_dict = {}

    for user in users_data:
        usr_id = str(user['id'])
        todo_dict[usr_id] = [
            {
                "username": user['username'],
                "task": task['title'],
                "completed": task['completed']
            }
            for task in todos_data if task['userId'] == user['id']
        ]

    with open("todo_all_employees.json", mode='w') as json_file:
        json.dump(todo_dict, json_file)
