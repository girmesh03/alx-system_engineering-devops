#!/usr/bin/python3
"""queries the Reddit API and returns a list containing the titles of all hot
articles for a given subreddit. If no results are found for the given
subreddit, the function should return None"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns a list containing the titles of all hot articles for a given
    subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None
    for post in response.json().get('data').get('children'):
        hot_list.append(post.get('data').get('title'))
    after = response.json().get('data').get('after')
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
