#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(user_id)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(user_id)).json()
    completed = [task for task in todo if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".
          format(user.get("name"), len(completed), len(todo)))
    for task in completed:
        print("\t {}".format(task.get("title")))
