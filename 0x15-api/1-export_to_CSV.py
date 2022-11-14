#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
if __name__ == "__main__":

    import requests
    import sys

    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        u_url = 'https://jsonplaceholder.typicode.com/users/'
        td_url = 'https://jsonplaceholder.typicode.com/todos?userId='

        USER_ID = requests.get(u_url + sys.argv[1]).json()['id']
        USERNAME = requests.get(u_url + sys.argv[1]).json()['username']
        TASK_COMPLETED_STATUSES = [task['completed'] for task in requests.
                                   get(td_url + sys.argv[1]).json()]
        TASKS_TITLES = [task['title'] for task in requests.
                        get(td_url + sys.argv[1]).json()]
        TOTAL_NUMBER_OF_TASKS = len(requests.get(td_url + sys.argv[1]).json())

        TASKS_LIST = ['"{}","{}","{}","{}"\n'.
                      format(USER_ID, USERNAME, TASK_COMPLETED_STATUSES[N],
                             TASKS_TITLES[N])
                      for N in range(TOTAL_NUMBER_OF_TASKS)]

        with open('{}.csv'.format(USER_ID), 'w') as test_file:
            for TASK_LIST in TASKS_LIST:
                test_file.write(TASK_LIST)
