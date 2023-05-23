#!/usr/bin/python3
"""Exports the data retrieved from the JSONPlaceholder API to JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(user_id)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(user_id)).json()

    to_json = {}
    to_json[user_id] = []
    for task in todo:
        to_json[user_id].append({"task": task.get("title"),
                                 "completed": task.get("completed"),
                                 "username": user.get("username")})

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(to_json, jsonfile)
