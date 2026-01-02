from src.services import TaskService


def print_menu():
    """Prints the main menu."""
    print("\n--- Todo CLI ---")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")
    print("----------------")


def add_task(task_service: TaskService):
    """Handles adding a new task."""
    title = input("Enter task title: ")
    if not title:
        print("Title cannot be empty.")
        return
    description = input("Enter task description (optional): ")
    task = task_service.add_task(title, description)
    print(f"Task '{task.title}' added with ID {task.task_id}.")


def view_all_tasks(task_service: TaskService):
    """Handles viewing all tasks."""
    tasks = task_service.get_all_tasks()
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- All Tasks ---")
    for task in tasks:
        status = "Completed" if task.status == task.status.COMPLETED else "Pending"
        print(f"ID: {task.task_id} | Title: {task.title} | Status: {status}")
        if task.description:
            print(f"  Description: {task.description}")
    print("-----------------")


def complete_task(task_service: TaskService):
    """Handles marking a task as completed."""
    try:
        task_id = int(input("Enter task ID to complete: "))
        task = task_service.complete_task(task_id)
        if task:
            print(f"Task {task_id} marked as completed.")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def update_task(task_service: TaskService):
    """Handles updating a task."""
    try:
        task_id = int(input("Enter task ID to update: "))
        new_title = input("Enter new title: ")
        if not new_title:
            print("Title cannot be empty.")
            return
        new_description = input("Enter new description (optional): ")
        task = task_service.update_task(task_id, new_title, new_description)
        if task:
            print(f"Task {task_id} updated.")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def delete_task(task_service: TaskService):
    """Handles deleting a task."""
    try:
        task_id = int(input("Enter task ID to delete: "))
        task = task_service.delete_task(task_id)
        if task:
            print(f"Task {task_id} deleted.")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def main():
    """Main application loop."""
    task_service = TaskService()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(task_service)
        elif choice == "2":
            view_all_tasks(task_service)
        elif choice == "3":
            complete_task(task_service)
        elif choice == "4":
            update_task(task_service)
        elif choice == "5":
            delete_task(task_service)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
