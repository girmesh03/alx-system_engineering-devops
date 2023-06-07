#!/usr/bin/python3
"""
recursive function that queries the Reddit API,
parses the title of all hot articles, and
prints a sorted count of given keywords
(case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
"""

import requests


def count_words(subreddit, word_list, array=None, after=""):
    """parses the title of all hot articles, and
    prints a sorted count of given keywords"""
    if array is None:
        array = [0] * len(word_list)
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return
    for post in response.json().get('data').get('children'):
        title = post.get('data').get('title')
        for i in range(len(word_list)):
            array[i] += title.lower().split(' ').count(word_list[i].lower())
    after = response.json().get('data').get('after')
    if after is None:
        for i in range(len(word_list)):
            if array[i] != 0:
                print("{}: {}".format(word_list[i], array[i]))
        return
    return count_words(subreddit, word_list, array, after)
