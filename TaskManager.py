#Initalise the list to store the tasks
tasks = []

#Create the needed functions
#1. Add function
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task was added successfully")

#2. Remove task
def remove_task():
    task = input("Enter the task you would like to romve: ")
    found = False 
    for i in tasks:
        if i == tasks:
            tasks.reomove(i)
            found = True
            print("Task was reomved from the list. ")
            break
        if not found:
            print("This task dpes not exits. ")

#3. View tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for i in tasks:
            print(i)
        
#The menu to display the options needed
while True:
    print("\nTask Manager")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        add_task()
    elif choice == 2:
        remove_task()
    elif choice == 3:
        view_tasks()
    elif choice == 4:
        print("Exiting the Task Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

