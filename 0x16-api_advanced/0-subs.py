#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
