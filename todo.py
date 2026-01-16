FILE_NAME = "tasks.txt"

def add_task():
    task = input("Enter task: ")
    with open(FILE_NAME, "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

def view_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks file found.")

def delete_task():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks to delete.")
            return

        view_tasks()
        task_no = int(input("Enter task number to delete: "))

        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            with open(FILE_NAME, "w") as file:
                file.writelines(tasks)
            print(f"Removed task: {removed.strip()}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")
    except FileNotFoundError:
        print("No tasks file found.")

def main():
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()
