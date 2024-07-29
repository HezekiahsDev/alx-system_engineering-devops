#!/usr/bin/python3
'''
get employees data from an API
'''

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            request_user = requests.get('{}/users/{}'.format(REST_API,
                id)).json()
            request_todo = requests.get('{}/todos'.format(REST_API)).json()
            request_name = request_user.get('name')
            track_tasks = list(filter(lambda x: x.get('userId') == id,
                request_todo))
            completed_tasks = list(filter(lambda x: x.get('completed'),
                track_tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    request_name,
                    len(completed_tasks),
                    len(track_tasks)
                )
            )
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))
