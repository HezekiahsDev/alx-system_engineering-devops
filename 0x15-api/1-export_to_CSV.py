#!/usr/bin/python3
"""Export detail from request to CSV file """
import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    api_url = 'https://jsonplaceholder.typicode.com/users/' + user
    res = requests.get(api_url)
    """ANYTHING"""
    user_name = res.json().get('username')
    task = api_url + '/todos'
    res = requests.get(task)
    tasks = res.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            """Complete"""
            task_title = task.get('title')
            """Done"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, task_title))
