# toDoApp.py

import os

tasks=[]

def add_task(task):
    """Task adding function"""
    tasks.append(task)
    print("task added!")

def show_tasks():
    """Show all tasks function"""
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def remove_task(tasknumber):
    """Task removing Function"""
    if tasknumber < 1 or tasknumber > len(tasks):
        print("Task does not exist!!")
        return
    tasks.pop(tasknumber-1)
    print("Task removed!!")

def main():
    """The running code"""
    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        ch = input("Enter Choice: ")
        if ch == "1":
            t = input("Enter Task: ")
            add_task(t)
        elif ch == "2":
            show_tasks()
        elif ch == "3":
            n=int(input("Enter a task to remove: "))
            remove_task(n)   
        elif ch == "4":
            break
        else:
            print("Wrong Choice!!")
        
        os.system("pause")
        os.system("cls")
main()
