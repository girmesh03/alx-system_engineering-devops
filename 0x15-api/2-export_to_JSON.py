#!/usr/bin/python3
"""Exports the data retrieved from the JSONPlaceholder API to JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    # Get the user id
    user_id = sys.argv[1]
    # Get the base url
    url = "https://jsonplaceholder.typicode.com/"
    # Get the user and todo
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "users/{}/todos".format(user_id)).json()

    # Create a dictionary
    to_dict = {
        user_id: [{"task": task.get("title"),
                   "completed": task.get("completed"),
                   "username": user.get("username")} for task in todo]
    }

    # Save the dictionary in a json file
    with open("{}.json".format(user_id), "w", newline="") as jsonfile:
        json.dump(to_dict, jsonfile)
