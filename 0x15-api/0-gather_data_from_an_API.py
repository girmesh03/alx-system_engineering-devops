#!/usr/bin/python3
"""Gather data from an API and Runs if the module is not imported"""
import requests
import sys

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f"{base_url}users/{sys.argv[1]}"
    # print(user_url)
    todos_url = f"{base_url}todos?userId={sys.argv[1]}"
    # print(todos_url)
    user_name = requests.get(user_url).json()['name']
    # print(user_name)
    todos_data = requests.get(todos_url).json()
    # print(todos_data)
    completed = 0
    total = 0
    completed_tasks = []
    for task in todos_data:
        total += 1
        if task['completed']:
            completed_tasks.append(task['title'])
            completed += 1

    print("Employee {} is done with tasks({}/{}):".format(
        user_name, completed, total))
    for task in completed_tasks:
        print("\t {}".format(task))
