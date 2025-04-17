# Author: Eyob Ollivierre


# File: office_task_app.py
# Date: 04/16/25
# Description: Console-based Office Task Manager that allows users to manage tasks dynamically
# using a priority queue (heap), hash map, and linked list-based data structure.

from task_structures import Task, TaskManager
from datetime import datetime

def parse_date(date_str):
    """
    Attempts to parse the user-entered date using multiple formats.
    Returns a datetime object if successful, else None.
    """
    formats = ['%Y-%m-%d', '%m/%d/%y', '%m/%d/%Y']
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None

def main():
    """
    Entry point of the application. Presents an interactive console menu
    for adding, viewing, and managing office tasks.
    """
    tm = TaskManager()
    print("\n📋 Welcome to the Office Task Manager!")

    while True:
        # Display user options
        print("\nMenu:")
        print("1. Add new task")
        print("2. Mark task as complete")
        print("3. View all tasks")
        print("4. View most urgent task")
        print("5. View completed tasks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            title = input("Enter task title: ").strip()
            due_date_str = input("Enter due date (e.g., 2025-04-17 or 4/17/25): ").strip()
            due_date = parse_date(due_date_str)
            if not due_date:
                print("❌ Invalid date format. Try using YYYY-MM-DD, MM/DD/YY, or MM/DD/YYYY.")
                continue
            try:
                priority = int(input("Enter priority (1 = High, 3 = Low): ").strip())
                if priority not in [1, 2, 3]:
                    raise ValueError
            except ValueError:
                print("❌ Invalid priority. Use 1, 2, or 3.")
                continue
            tm.add_task(title, due_date.strftime("%Y-%m-%d"), priority)

        elif choice == '2':
            task_id = input("Enter Task ID to mark complete (e.g., T1): ").strip()
            tm.mark_task_complete(task_id)

        elif choice == '3':
            tm.show_all_tasks()

        elif choice == '4':
            urgent = tm.get_most_urgent_task()
            if urgent:
                print("\n🔥 Most Urgent Task:")
                print(urgent)
            else:
                print("No tasks available.")

        elif choice == '5':
            tm.show_completed_tasks()

        elif choice == '6':
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select a number from 1 to 6.")

if __name__ == "__main__":
    main()
