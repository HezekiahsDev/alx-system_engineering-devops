#!/usr/bin/python3
""" Export response from API into a CSV file"""
import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    api_url = 'https://jsonplaceholder.typicode.com/users/' + user
    usr_req = requests.get(api_url)

    """Initialize parameters"""
    user_name = api_req.json().get('username')
    task = api_url + '/todos'
    todo_req = requests.get(task)
    tasks = todo_req.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tasks:
            completed_tasks = task.get('completed')
            """Complete"""
            title_task = task.get('title')
            """Done"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed_tasks, title_task))
