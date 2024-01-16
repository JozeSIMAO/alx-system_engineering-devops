#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit.
"""
import requests
from sys import argv

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-app/0.0.1'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        for post in data:
            print(post.get('data', {}).get('title'))
    else:
        print(None)


if __name__ == '__main__':
    top_ten = __import__('1-top_ten').top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
