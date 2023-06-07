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
    """parses the title of all hot articles,
    and prints a sorted count of given keywords"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return
    if array is None:
        array = []
        for word in word_list:
            array.append([word, 0])
    for post in response.json().get('data').get('children'):
        title = post.get('data').get('title').lower().split()
        for word in word_list:
            for t in title:
                if word.lower() == t:
                    for a in array:
                        if a[0] == word:
                            a[1] += 1
    after = response.json().get('data').get('after')
    if after is None:
        for a in sorted(array, key=lambda x: x[1], reverse=True):
            if a[1] != 0:
                print("{}: {}".format(a[0], a[1]))
        return
    return count_words(subreddit, word_list, array, after)
