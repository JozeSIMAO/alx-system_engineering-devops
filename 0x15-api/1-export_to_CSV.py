#!/usr/bin/python3
"""Export data to CSV"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{base_url}/users/{user_id}")
    todos_response = requests.get(f"{base_url}/todos?userId={user_id}")

    user_data = user_response.json()
    todos_data = todos_response.json()

    csv_file = f"{user_id}.csv"

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([user_id, user_data['username'],
                             task['completed'], task['title']])
