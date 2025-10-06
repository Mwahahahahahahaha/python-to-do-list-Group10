# todo_app.py

import os

tasks=[]

def add_task(task):
    """Task adding function"""
    tasks.append(task)
    print("The task has been added!")

def show_tasks():
    """Show all tasks function"""
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def remove_task(task_number):
    """Task removing Function"""
    try:
        tasks.pop(task_number-1)
        print("Task removed!!")
    except IndexError:
        print("Failed to delete task. There is no task associated the specified index")

def main():
    """The running code"""
    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        ch = input("Enter Choice: ")
        if ch == "1":
            task = input("Enter Task: ")
            add_task(task)
        elif ch == "2":
            show_tasks()
        elif ch == "3":
            try:
                index= int(input("Enter the index of the task to be removed: "))
                remove_task(index)
            except ValueError:
                print("The input must be an integer!")
        elif ch == "4":
            break
        else:
            print("Wrong Choice!!")

        os.system("pause")
        os.system("cls")
main()
