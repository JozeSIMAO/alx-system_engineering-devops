#!/usr/bin/python3
"""
Gather data from an API
"""

import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get("{}/users/{}".format(base_url, user_id))
    todos_response = requests.get("{}/todos?userId={}".
                                  format(base_url, user_id))

    user_data = user_response.json()
    todos_data = todos_response.json()

    completed_tasks = [task for task in todos_data if task['completed']]
    total_tasks = len(todos_data)

    print("Employee {} is done with tasks({}/{})".
          format(user_data['name'], len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t{}".format(task['title']))
