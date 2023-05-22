#!/usr/bin/python3
"""Gather data from an API and returns a todo based on the given user id"""
import requests
import sys

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f"{base_url}users/{sys.argv[1]}"
    todos_url = f"{base_url}todos?userId={sys.argv[1]}"
    user_name = requests.get(user_url).json()['name']
    todos_data = requests.get(todos_url).json()
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
