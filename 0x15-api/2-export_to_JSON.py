#!/usr/bin/python3
"""Convet api response to JSON"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    api_url = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    res = requests.get(api_url)
    """Username from API"""
    USERNAME = res.json().get('username')
    """Use todo from api"""
    todo_path = url_to_user + '/todos'
    res = requests.get(todo_path)
    tasks = res.json()

    stored_data = {USER_ID: []}
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        stored_data[USER_ID].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": USERNAME})
    """print(dict_data)"""
    with open('{}.json'.format(USER_ID), 'w') as f:
        json.dump(stored_data, f)
