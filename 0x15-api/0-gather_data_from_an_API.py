#!/usr/bin/python3
"""
Gather data from an API
"""

import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{base_url}/users/{user_id}")
    todos_response = requests.get(f"{base_url}/todos?userId={user_id}")

    user_data = user_response.json()
    todos_data = todos_response.json()

    completed_tasks = [task for task in todos_data if task['completed']]
    total_tasks = len(todos_data)

    print(f"Employee {user_data['name']} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")
