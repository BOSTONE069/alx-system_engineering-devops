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

        employee_name = requests.get(u_url + sys.argv[1]).json()['name']
        number_of_done_tasks = len([task for task in requests.
                                   get(td_url + sys.argv[1]).json()
                                    if task['completed'] is True])
        total_number_of_tasks = len(requests.get(td_url + sys.argv[1]).json())
        done_tasks_titles = [task['title'] for task in requests.get(td_url + sys.argv[1]).json()
                             if task['completed'] is True]

        print(f"Employee {employee_name} is done with task"
              f"({number_of_done_tasks}/{total_number_of_tasks}):")
        for task_title in done_tasks_titles:
            print(f"\t {task_title}")
