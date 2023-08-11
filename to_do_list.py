"""
    To - do - list

    functions
        add_task(data) - Adding the task in the list
        update_task(index,new_data) - Update a task from the list
        show_task() - show the list
        delete_task(index) - Delete a task from the list
"""
import os
import time
from datetime import datetime
from colorama import Fore, Style

def animation(message, duration=1):
    """
        Animation
    """
    print(message, end='',flush=True)
    for _ in range(3):
        time.sleep(duration/4)
        print('.',end='',flush=True)
    print()

def add_task(tasks,data):
    """
        Add task
    """
    date = datetime.now()
    task_data = {'task': data, 'timestamp':date}
    tasks.append(task_data)
    print(f'{Fore.GREEN}Task Added:{Style.RESET_ALL} {data} (Added: {date})')

def update_task(tasks,i,data):
    """
        Update task
    """
    if i<1 or i>len(tasks):
        print('{Fore.RED}Invalid Index. No task updated.{Style.RESET_ALL}')
    else:
        tasks[i - 1]['task'] = data
        print(f'{Fore.GREEN}Task Updated:{Style.RESET_ALL} {data}')

def show_task(tasks):
    """
        Show Task
    """
    if not tasks:
        print(f'{Fore.YELLOW}No tasks assigned yet...{Style.RESET_ALL}')
    else:
        print(f'{Fore.BLUE}Tasks:{Style.RESET_ALL}')
        for i, task_data in enumerate(tasks,start = 1):
            task = task_data['task']
            timestamp = task_data.get('timestamp')
            if timestamp:
                formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
                print(f'{i}. {task} (Added: {formatted_timestamp})')
            else:
                print(f'{i}. {task}')
        print()
        time.sleep(4)

def delete_task(tasks,i):
    """
        Delete Task
    """
    if i<1 or i>len(tasks):
        print('Enter Valid Number......')
    else:
        confirm = input(f"Are you sure you want to delete task {i}? (yes/no): ")
        if confirm.lower() == 'yes':
            deleted_task = tasks.pop(i - 1)
            print(f'{Fore.YELLOW}Deleted task:{Style.RESET_ALL} {deleted_task}')
        else:
            print(f'{Fore.YELLOW}Task deletion canceled.{Style.RESET_ALL}')

def save_tasks(tasks, filename='tasks.txt'):
    """
        Save Task to a file 
    """
    with open(filename, 'w') as file:
        for task_data in tasks:
            task = task_data['task']
            timestamp = task_data.get('timestamp')
            if timestamp:
                formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
                file.write(f'{task} ({formatted_timestamp})\n')
            else:
                file.write(f"{task}\n")

def load_tasks(filename='tasks.txt'):
    """
    Load tasks from the file
    """
    tasks = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                task_data = {'task': line}
                if '(' in line and ')' in line:
                    task, timestamp_str = line.split('(', 1)
                    task_data['task'] = task.strip()
                    task_data['timestamp'] = datetime.strptime(timestamp_str.strip(') '), '%Y-%m-%d %H:%M:%S')
                tasks.append(task_data)
    except FileNotFoundError:
        pass
    return tasks


if __name__ == '__main__':
    menu_tasks = load_tasks()

    while True:
        os.system('cls')
        print('To-do-List'.center(50,'_'))
        MENU = '''
            \n options:
            1. Add Task
            2. Update Task
            3. Show Task
            4. Delete Task
            5. Exit
        '''
        try:
            print(MENU)
            choice = int(input(f'{Fore.BLUE}Enter your choice (1/2/3/4/5): {Style.RESET_ALL}'))
            if choice == 1:
                add_task(menu_tasks,
                         input(f'{Fore.BLUE}Enter the task you want to add:{Style.RESET_ALL}'))
                save_tasks(menu_tasks)
                animation('Adding Task',2)
            elif choice == 2:
                update_task(menu_tasks,
                            int(input(f'{Fore.BLUE}Enter task index to update:{Style.RESET_ALL}')),
                            input(f'{Fore.BLUE}Enter new task: {Style.RESET_ALL}'))
                save_tasks(menu_tasks)
                animation('Updating Task',1)
            elif choice == 3:
                show_task(menu_tasks)
                animation('Loading Task',1)
            elif choice == 4:
                delete_task(menu_tasks,
                            int(input(f"{Fore.BLUE}Enter Index of task that u wanna remove:\
{Style.RESET_ALL}")))
                save_tasks(menu_tasks)
                animation('Deleting task',1)
            elif choice == 5:
                print(f'{Fore.YELLOW}Exiting.....{Style.RESET_ALL}')
                break
            else:
                print(f'{Fore.RED}Invalid choice...Please try again...{Style.RESET_ALL}')
            time.sleep(2)
        except ValueError as ve:
            print(f'{Fore.RED}Invalid input: {ve}{Style.RESET_ALL}')
            time.sleep(2)
        except IndexError as ie:
            print(f'{Fore.RED}Index out of range: {ie}{Style.RESET_ALL}')
            time.sleep(2)
        except Exception as e:
            print(f'{Fore.RED}Warning! Error due to {e}{Style.RESET_ALL}')
            time.sleep(2)
