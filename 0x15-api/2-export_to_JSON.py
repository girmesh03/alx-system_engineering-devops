#!/usr/bin/python3
"""Exports the data retrieved from the JSONPlaceholder API to JSON format"""

import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users/{}".format(url, user_id)).json()
    todo = requests.get("{}users/{}/todos".format(url, user_id)).json()

    # Create a dictionary
    to_dict = {
        user_id: [{"task": task.get("title"),
                   "completed": task.get("completed"),
                   "username": user.get("username")} for task in todo]
    }

    # Save the dictionary in a json file
    with open("{}.json".format(user_id), "w", newline="") as jsonfile:
        json.dump(to_dict, jsonfile)
