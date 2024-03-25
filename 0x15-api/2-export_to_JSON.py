#!/usr/bin/python3
"""export data in the JSON format"""

import json
import requests
import sys


if __name__ == '__main__':
    Id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    url += "/" + Id
    response = requests.get(url)
    username = response.json().get('username')
    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    dic = {Id: []}
    for task in tasks:
        dic[Id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(Id), 'w') as file:
        json.dump(dic, file)
