#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot
    posts listed for a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print("None")
        return
    for post in response.json().get('data').get('children'):
        print(post.get('data').get('title'))
