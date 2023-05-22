#!/usr/bin/python3
"""Exports the data retrieved from the JSONPlaceholder API to JSON format
by extending task 0."""
import json
import requests


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    to_json = {}
    for user in users:
        user_id = user.get("id")
        to_json[user_id] = []
        for task in todo:
            if task.get("userId") == user_id:
                to_json[user_id].append({"task": task.get("title"),
                                         "completed": task.get("completed"),
                                         "username": user.get("username")})

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(to_json, jsonfile)
