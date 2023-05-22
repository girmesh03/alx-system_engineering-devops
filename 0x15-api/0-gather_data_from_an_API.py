#!/usr/bin/python3
"""Gather data from an API and Runs if the module is not imported"""
import requests
import sys

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f"{base_url}users/{sys.argv[1]}"
    todos_url = f"{base_url}todos?userId={sys.argv[1]}"

    try:
        user_data = requests.get(user_url).json()
        todos_data = requests.get(todos_url).json()

        user_name = user_data.get('name')

        completed = 0
        total = 0
        completed_tasks = []

        for task in todos_data:
            total += 1
            if task.get('completed'):
                completed_tasks.append(task.get('title'))
                completed += 1

        print("Employee {} is done with tasks({}/{}):".format(
            user_name, completed, total))

        for task in completed_tasks:
            print("\t{}".format(task))

    except requests.exceptions.RequestException:
        pass

    except (KeyError, IndexError):
        pass
