import argparse
import json
from datetime import datetime

parser = argparse.ArgumentParser(
    prog="tasktracker",
    description="A simple CLI task tracker",
)

subparsers = parser.add_subparsers(dest='command', help='Available commands')

#add command
add_parser = subparsers.add_parser('add', help='Add new task')
add_parser.add_argument('title', help='Name of task')
add_parser.add_argument('-s', '--status', choices=['todo', 'in-progress', 'done'], default='todo', help='Status of the task')

#update command
add_parser = subparsers.add_parser('update', help='Update task')
add_parser.add_argument('id', help='Choose task id to update info')
add_parser.add_argument('-t', '--title', help="Change task's name")
add_parser.add_argument('-s', '--status', choices=['todo', 'in-progress', 'done'], help='Status of the task')

#delete command
add_parser = subparsers.add_parser('delete', help='Delete task')
add_parser.add_argument('id', help='Delete task by id')

#list command
list_parser = subparsers.add_parser('list', help='Shows tasks')
list_parser.add_argument('-s', '--status', choices=['done', 'in-progress', 'todo'], default='all', help='Add specification by tasks status')

args = parser.parse_args()

def list_tasks(status = 'all'):
    if status == 'all':
        try:
            with open("tasks.json", 'r') as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            data = dict()
            with open("tasks.json", 'w') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
                return data
    else:
        with open("tasks.json", 'r') as f:
            data = json.load(f)
            sorted_data = dict()
            for x, y in data.items():
                if y['status'] == status:
                    sorted_data[x] = y
            return sorted_data

def list_tasks_user(status = 'all'):
    data = list_tasks(status)
    for id, info in data.items():
        print(id, info['title'], info['status'], info['update_time'], info['create_time'], sep='\t', end='\n')


def add_task(title, status = 'todo'):
    data = list_tasks()
    create_time = datetime.today().isoformat(sep=' ', timespec='seconds')
    update_time = create_time
    if not data:
        new_id = 1
    else:
        new_id = int(list(data.keys())[-1]) + 1
    maininfo = {'title': title,
                'status': status,
                'update_time': update_time,
                'create_time': create_time}
    data[new_id] = maininfo
    with open("tasks.json", 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def update_task(id, title, status):
    data = list_tasks()
    if not data:
        return "No data was found"
    else:
        if id not in data:
            print("Wrong id number")
            return None
        update_time = datetime.today().isoformat(sep=' ', timespec='seconds')
        if title:
            data[id]['title'] = title
        if status:
            data[id]['status'] = status
        data[id]['update_time'] = update_time
    with open("tasks.json", 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def delete_task(id):
    data = list_tasks()
    if not data:
        return "No data was found"
    elif id not in data:
        print("Wrong id number")
        return None
    else:
        del data[id]
    with open("tasks.json", 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def main():
    if args.command == 'add':
        add_task(args.title, args.status)
    elif args.command == 'list':
        list_tasks_user(args.status)
    elif args.command == 'update':
        update_task(args.id, args.title, args.status)
    elif args.command == 'delete':
        delete_task(args.id)
    else:
        print('Irregular command input, try again')

if __name__ == '__main__':
    main()