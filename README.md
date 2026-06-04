# task_tracker
A simple CLI task tracker to manage tasks by marking their statuses like todo, in-progress, and done

# Installation
CLI command "pip install git+https://github.com/T0Rt52/task_tracker.git"

# Usage
tasktracker -h --help shows usage of the app
tasktracker add ["Task title"] [-s, --status] adds task in list, "todo" status by default
tasktracker update ["id"] [-s, --status] [-t, --title] updates task's status or/and title by id
tasktracker delete ["id"] deletes task by id
tasktracker list [-s, --status] demonstrates list of tasks, could be sorted by status
there are only 3 awaiable status for the task - 'todo', 'in-progress', 'done'

# Example
tasktracker add "Cook dinner"
tasktracker add "Do push-ups" -s in-progress
tasktracker update 1 -t "Watch a movie" -s done
tasktracker delete 1
tasktracker list
tasktracker list -s done
