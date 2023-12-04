import time

tasks = ["Go to shopping", "Call the parents", "Do homework"]
task_details = {"Go to shopping": ("3rd December", 5),
                "Call the parents": ("9th December", 3),
                "Do homework": ("8th December", 4)
                }


def add_task():
    print("Please enter the task and task details")
    task = input("Task: ")

    tasks.append(task)

    task_date = input("Date: ")

    while True:
        try:
            task_priority = int(input("Priority(5-Very important, 1-Not important): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    task_details[task] = task_date, task_priority
    print("Task added successfully!")

    """
    print("Test: ", tasks)  # Test
    print("Test: ", task_details)  # Test
    """

def update_task():
    print("*" * 30)
    time.sleep(0.5)

    if not tasks:
        print("No tasks available.")
        return

    for i, task_name in enumerate(tasks, 1):
        print(f"{i}-{task_name}")

    print("*" * 30)

    try:
        selection = int(input("Choose a task: "))
        selected_task = tasks[selection - 1]
    except (ValueError, IndexError):
        print("Invalid selection. Please choose a valid task.")
        return

    print("Here, you can see the details of the chosen task.")
    time.sleep(0.5)
    print(task_details[selected_task])

    task_new_date = input("Enter new date: ")

    while True:
        try:
            task_new_priority = int(input("Enter new priority(5-Very important, 1-Not important): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    task_details[selected_task] = task_new_date, task_new_priority
    print("Task updated successfully!")


def delete_task():
    print("*" * 30)
    time.sleep(0.5)

    if not tasks:
        print("No tasks available.")
        return

    for i, task_name in enumerate(tasks, 1):
        print(f"{i}-{task_name}")

    print("*" * 30)

    try:
        selection = int(input("Choose a task for deletion: "))
        deleted_task = tasks.pop(selection - 1)
        del task_details[deleted_task]
        print(f"Task '{deleted_task}' deleted successfully!")
    except (ValueError, IndexError):
        print("Invalid selection. Please choose a valid task.")


def print_tasks(task_list):
    for i, task in enumerate(task_list, 1):
        print(f"Task {i}".center(30, "="))
        print(f"Name: {task}\n"
              f"Date: {task_details[task][0]}\n"
              f"Priority: {task_details[task][1]}")
        time.sleep(0.4)
    print("".center(30, "="))


def show_tasks():
    subprocess = input('A-Show the all tasks\n'
                       'B-Show the sorted tasks (5 to 1)\n'
                       'Choose an option: ').upper()

    time.sleep(0.2)

    if subprocess == "A":
        print_tasks(tasks)
    elif subprocess == "B":
        sorted_list = sorted(tasks, key=lambda task: task_details[task][1], reverse=True)
        print_tasks(sorted_list)
    else:
        print("Invalid option. Please choose A or B.")


while True:
    transaction = input("1-Add Task\n"
                        "2-Update Task\n"
                        "3-Show To-do List\n"
                        "4-Delete Task\n"
                        "0-Exit\n"
                        "Select a transaction:")
    if transaction == "1":
        add_task()
    elif transaction == "2":
        update_task()
    elif transaction == "3":
        show_tasks()
    elif transaction == "4":
        delete_task()
    elif transaction == "0":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid selection. Please choose a valid option.")
