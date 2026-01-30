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
    if not tasks:
        print("No tasks to remove.")
        return
    view_tasks()
    try:
      task_num = int(input("Enter the task number to remove: "))
      index = task_num - 1
      if index < 0 or index >= len(tasks):
          print("Invalid task number.")
      else:
            removed_task = tasks.pop(index) #A built in function to remove an item from a list at a specific index
            print(f"Task '{removed_task}' was removed successfully.")
    except ValueError:
        print("Please enter a valid number.")
    
        
#3. View tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        
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
        print("The number of tasks: ", len(tasks))
    elif choice == 2:
        remove_task()
    elif choice == 3:
        view_tasks()
    elif choice == 4:
        print("Are you sure you want to exit? (yes/no)")
        confirm = input("Enter your choice: ").lower()
        if confirm == "yes":
            print("Exising the task manager, goobye!. ") 
            break
        else:
            continue
    else:
        print("Invalid choice. Please try again.")

