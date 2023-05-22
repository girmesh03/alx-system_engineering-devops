#!/usr/bin/python3
"""Gather data from an API and Runs if the module is not imported"""
import requests
import sys


def fetch_user_todos(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f"{base_url}users/{employee_id}"
    todos_url = f"{base_url}todos"

    response = requests.get(user_url)
    response.raise_for_status()
    user_data = response.json()

    response = requests.get(todos_url, params={"userId": employee_id})
    response.raise_for_status()
    todos_data = response.json()

    return user_data, todos_data


def print_todo_progress(user_data, todos_data):
    completed_tasks = [task['title']
                       for task in todos_data if task['completed']]
    completed = len(completed_tasks)
    total = len(todos_data)

    print("Employee {} is done with tasks({}/{}):".format(
        user_data['name'], completed, total))
    for task in completed_tasks:
        print(f"\t{task}")


if __name__ == "__main__":
    employee_id = sys.argv[1]

    try:
        user_data, todos_data = fetch_user_todos(employee_id)
        print_todo_progress(user_data, todos_data)
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e.response.status_code} - {e.response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
