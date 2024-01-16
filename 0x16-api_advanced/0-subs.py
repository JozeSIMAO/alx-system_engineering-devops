#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers (not active users,
total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
        returns the number of subscribers for a given subreddit
    '''
    user = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])