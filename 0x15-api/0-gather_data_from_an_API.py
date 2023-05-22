#!/usr/bin/python3
"""Gather data from an API and Runs if the module is not imported"""
import requests
import sys

if __name__ == "__main__":
    """Gather data from an API"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "todos", params={"userId": user_id}).json()
    completed = [task for task in todo if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todo)))
    for task in completed:
        print("\t {}".format(task.get("title")))
