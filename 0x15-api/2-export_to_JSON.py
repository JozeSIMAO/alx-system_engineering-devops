#!/usr/bin/python3
"""
Export data to JSON
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{base_url}/users/{user_id}")
    todos_response = requests.get(f"{base_url}/todos?userId={user_id}")

    user_data = user_response.json()
    todos_data = todos_response.json()

    json_data = {user_id: []}

    for task in todos_data:
        json_data[user_id].append({"task": task['title'], "completed":
                                   task['completed'],
                                   "username": user_data['username']})

    with open(f"{user_id}.json", mode='w') as json_file:
        json.dump(json_data, json_file)
