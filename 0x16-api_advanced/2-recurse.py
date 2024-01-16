#!/usr/bin/python3
"""
recursive function that queries the
Reddit API and returns a list containing the titles of all hot
articles for a given subreddit. If no results are found for the
given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-app/0.0.1'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        if not data:
            return hot_list
        else:
            after = data[-1].get('data', {}).get('name')
            hot_list.extend([post.get('data',
                                      {}).get('title') for post in data])
            return recurse(subreddit, hot_list, after)
    else:
        return None


if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
