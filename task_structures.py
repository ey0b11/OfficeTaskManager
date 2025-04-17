# Author: Eyob Ollivierre

# Date: 4/14/24
# File: task_structures.py


### Description: Core data structures for the Office Task Manager project.
###
#
#Includes Task class and TaskManager class which handles task logic
#using a heap (priority queue), a hash map, and a list.
###


import heapq
from datetime import datetime


class Task:
    """
    Represents a single task with an ID, title, due date, priority, and completion status.
    """

    def __init__(self, task_id, title, due_date_str, priority):
        """
        Initializes a new Task object.

        Args:
            task_id (str): Unique identifier for the task (e.g., T1, T2).
            title (str): Title or name of the task.
            due_date_str (str): Due date of the task in 'YYYY-MM-DD' format.
            priority (int): Task priority level (1 = High, 2 = Medium, 3 = Low).
        """
        self.id = task_id
        self.title = title
        self.due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        self.priority = priority
        self.completed = False

    def __lt__(self, other):
        """
        Enables heapq to compare tasks based on priority and due date.

        Returns:
            bool: True if this task is more urgent than the other.
        """
        return (self.priority, self.due_date) < (other.priority, other.due_date)

    def __str__(self):
        """
        String representation of a task.

        Returns:
            str: Formatted string of task details.
        """
        status = "✓" if self.completed else "X"
        return (f"{self.id} | {self.title} | Due: {self.due_date.date()} | "
                f"Priority: {self.priority} | Done: {status}")


class TaskManager:
    """
    Manages all tasks using a priority queue, hash map, and list.
    Supports adding, completing, and displaying tasks.
    """

    def __init__(self):
        """
        Initializes the TaskManager with empty structures.
        """
        self.tasks = {}          # HashMap: task_id -> Task
        self.task_list = []      # LinkedList simulation (simple list)
        self.task_heap = []      # PriorityQueue: Min-heap based on priority/due date
        self.completed = []      # List of completed tasks (order preserved)
        self.task_counter = 1    # Auto-generated task ID tracker

    def add_task(self, title, due_date_str, priority):
        """
        Adds a new task to the system.

        Args:
            title (str): Task title.
            due_date_str (str): Due date in 'YYYY-MM-DD'.
            priority (int): 1 = High, 2 = Medium, 3 = Low
        """
        task_id = f"T{self.task_counter}"
        self.task_counter += 1
        task = Task(task_id, title, due_date_str, priority)

        self.tasks[task_id] = task
        self.task_list.append(task)
        heapq.heappush(self.task_heap, task)

        print(f"\n✅ Task '{title}' added successfully with ID {task_id}.")

    def mark_task_complete(self, task_id):
        """
        Marks a specific task as complete by ID.

        Args:
            task_id (str): Task ID to mark complete.
        """
        if task_id in self.tasks:
            task = self.tasks[task_id]
            task.completed = True
            self.completed.append(task)
            print(f"\n✔️ Task '{task.title}' marked complete.")
        else:
            print("\n⚠️ Task ID not found.")

    def show_all_tasks(self):
        """
        Displays all tasks currently in the task manager.
        """
        if not self.task_list:
            print("\n📭 No tasks available.")
            return
        print("\n🗂️ All Tasks:")
        for task in self.task_list:
            print("  ", task)

    def show_completed_tasks(self):
        """
        Displays all completed tasks, in the order they were completed.
        """
        if not self.completed:
            print("\n📭 No tasks have been completed yet.")
            return
        print("\n✅ Completed Tasks (in order):")
        for task in self.completed:
            print("  ", task)

    def get_most_urgent_task(self):
        """
        Returns the most urgent incomplete task based on priority and due date.

        Returns:
            Task or None: The most urgent task or None if none found.
        """
        while self.task_heap:
            task = heapq.heappop(self.task_heap)
            if not task.completed:
                return task
        return None
