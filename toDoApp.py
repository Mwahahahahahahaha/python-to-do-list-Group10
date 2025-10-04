# toDoApp.py

import os

tasks=[]

def addtask(task) :
  tasks.append(task)
  print("task added!")

def showTasks():
    if len(tasks) == 0:
        print("No Tasks Yet")
    else:
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

def removetask(tasknumber):
    tasks.pop(tasknumber) 
    print("Task Removed!!")

def main():
    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        ch = input("Enter Choice: ")
        if ch == "1":
            t = input("Enter Task: ")
            addtask(t)
        elif ch == "2":
            showTasks()
        elif ch == "3":
            n = int(input("enter task no to remove: "))
            removetask(n)   
        elif ch == "4":
            break
        else:
            print("wrong choice!!")
        os.system("pause")
        os.system("cls")
main()
