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
add_parser.add_argument('-s', '--status', choices=['todo', 'in-progress', 'done'], default='todo', help='status of the task')

#update command
add_parser = subparsers.add_parser('update', help='Update task')
add_parser.add_argument('id', help='Choose task id to update info')
add_parser.add_argument('-t', '--title', help="Change task's name")
add_parser.add_argument('-s', '--status', choices=['todo', 'in-progress', 'done'], help='status of the task')

#delete command
add_parser = subparsers.add_parser('delete', help='Delete task')
add_parser.add_argument('id', help='Delete task by id')

#list command
list_parser = subparsers.add_parser('list', help='shows tasks')

args = parser.parse_args()

def list_tasks():
    try:
        with open("tasks.json", 'r') as f:
            data = json.load(f)
            return data
    except Exception as e:
        return e

def add_task(title, status = 'todo'):
    data = list_tasks()
    create_time = datetime.today().isoformat(sep='T', timespec='seconds')
    update_time = create_time
    if isinstance(data, dict):
        data['id'].append(data['id'][-1] + 1)
        data['title'].append(title)
        data['status'].append(status)
        data['update_time'].append(update_time)
        data['create_time'].append(create_time)
    else:
        data = {}
        data['id'] = [1]
        data['title'] = [title]
        data['status'] = [status]
        data['update_time'] = [update_time]
        data['create_time'] = [create_time]
    with open("tasks.json", 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def update_task(id, title, status):
    data = list_tasks()
    if not isinstance(data, dict):
        print(data)
        return None
    else:
        update_time = datetime.today().isoformat(sep='T', timespec='seconds')
        if title:
            data['title'][int(id) - 1] = title
        if status:
            data['status'][int(id) - 1] = status
        data['update_time'][int(id) - 1] = update_time
    with open("tasks.json", 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def delete_task(id):
    data = list_tasks()
    if not isinstance(data, dict):
        print(data)
        return None
    else:
        data['id'].pop(int(id) - 1)
        data['title'].pop(int(id) - 1)
        data['status'].pop(int(id) - 1)
        data['update_time'].pop(int(id) - 1)
        data['create_time'].pop(int(id) - 1)
        data['id'] = [x for x in range(1, len(data['id']) + 1)]
    with open("tasks.json", 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if args.command == 'add':
    add_task(args.title, args.status)
elif args.command == 'list':
    print(list_tasks())
elif args.command == 'update':
    update_task(args.id, args.title, args.status)
elif args.command == 'delete':
    delete_task(args.id)
else:
    print('Irregular command input, try again')