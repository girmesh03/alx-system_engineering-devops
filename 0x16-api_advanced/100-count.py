#!/usr/bin/python3
"""
recursive function that queries the Reddit API,
parses the title of all hot articles, and
prints a sorted count of given keywords
(case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
"""

import requests


def count_words(subreddit, word_list, after=None, word_dict={}):
    """parses the title of all hot articles, and
    prints a sorted count of given keywords"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'after': after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data")
        after = results.get("after")

        for child in results.get("children"):
            title = child.get("data").get("title")
            for word in word_list:
                ocurrences = title.lower().split().count(word.lower())
                if ocurrences > 0:
                    if word in word_dict:
                        word_dict[word] += ocurrences
                    else:
                        word_dict[word] = ocurrences

        if after is not None:
            return count_words(subreddit, word_list, after, word_dict)
        else:
            if len(word_dict) == 0:
                return
            for key, value in sorted(word_dict.items(),
                                     key=lambda item: item[1],
                                     reverse=True):
                print("{}: {}".format(key.lower(), value))
