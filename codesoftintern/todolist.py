def display_tasks(tasks):
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("\nTo-do List:")
        for index, task in enumerate(tasks,start=1):
            print(f"{index}. {task}")

def add_task(tasks,new_tasks):
    tasks.append(new_tasks)
    print(f"Task '{new_tasks}' added to the to-do list.")

def remove_task(tasks,task_index):
    if 1 <= task_index <= len(tasks):
        remove_task = tasks.pop(task_index - 1)
        print(f"Task '{remove_task}' removed from the to-do list.")
    else:
        print("Invalid task index.")

def main():
    tasks = []

    while True:
        print("\nSelect an option:")
        print("1. Display tasks\n2. Add tasks\n3. Remove tasks\n4. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            new_task = input("Enter the new task: ")
            add_task(tasks,new_task)
        elif choice == '3':
            task_index = int(input("Enter the number to remove a task: "))
            remove_task(tasks, task_index)
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ =="__main__":
    main()
