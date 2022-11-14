#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about to do list
"""
if __name__ == "__main__":

    import requests
    import sys

    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        u_url = 'https://jsonplaceholder.typicode.com/users/'
        td_url = 'https://jsonplaceholder.typicode.com/todos?userId='

        EMPLOYEE_NAME = requests.get(u_url + sys.argv[1]).json()['name']
        NUMBER_OF_DONE_TASKS = len([task for task in requests.
                                    get(td_url + sys.argv[1]).json()
                                    if task['completed'] is True])
        TOTAL_NUMBER_OF_TASKS = len(requests.get(td_url + sys.argv[1]).json())
        DONE_TASKS_TITLES = [task['title'] for task in requests.
                             get(td_url + sys.argv[1]).json()
                             if task['completed'] is True]

        print('Employee {} is done with tasks({}/{}):'.
              format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS,
                     TOTAL_NUMBER_OF_TASKS))
        for TASK_TITLE in DONE_TASKS_TITLES:
            print('\t {}'.format(TASK_TITLE))
