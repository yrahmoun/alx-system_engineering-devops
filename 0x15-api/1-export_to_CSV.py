#!/usr/bin/python3
"""export data in the CSV format"""

import requests
import sys


if __name__ == '__main__':
    Id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + Id
    response = requests.get(url)
    username = response.json().get('username')
    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    with open('{}.csv'.format(Id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(Id, username, task.get('completed'),
                               task.get('title')))
