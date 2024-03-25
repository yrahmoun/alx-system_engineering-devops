#!/usr/bin/python3
"""returns information about employee"""

import requests
import sys


if __name__ == '__main__':
    Id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + Id
    response = requests.get(url)
    name = response.json().get('name')
    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    count = 0
    task_list = []
    for task in tasks:
        if task.get('completed'):
            task_list.append(task)
            count += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, count, len(tasks)))
    for task in task_list:
        print("\t {}".format(task.get('title')))
