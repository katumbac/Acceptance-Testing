#Katherine Tumbaco
from datetime import datetime

class Task:
    def __init__(self, description, priority="Medium", status="Pending"):
        self.description = description
        self.priority = priority
        self.status = status
        self.creation_date = datetime.now()

    def mark_completed(self):
        self.status = "Completed"

    def mark_pendiente(self):
        self.status = "Pending"

    def update_priority(self, new_priority):
        self.priority = new_priority

    def __str__(self):
        return (f"{self.description} (Priority: {self.priority}, "
                f"Status: {self.status}, Created on: {self.creation_date.strftime('%Y-%m-%d %H:%M:%S')})")


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority="Medium"):
        self.tasks.append(Task(description, priority))

    def list_tasks(self):
        return self.tasks

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                return True
        return False
    
    def mark_task_pendiente(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_pendiente()
                return True
        return False

    def clear_list(self):
        self.tasks = []

    def list_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

    def remove_task(self, description):
        self.tasks = [task for task in self.tasks if task.description != description]

    def list_tasks_by_status(self, status):
        return [task for task in self.tasks if task.status == status]

    def update_task_priority(self, description, new_priority):
        for task in self.tasks:
            if task.description == description:
                task.update_priority(new_priority)
                return True
        return False


def print_summary(todo_list):
    print("To-Do List Summary")
    print("All tasks:")
    for task in todo_list.list_tasks():
        print(f"- {task}")

    print("\nTasks with priority 'High':")
    for task in todo_list.list_tasks_by_priority("High"):
        print(f"- {task}")

    print("\nTasks that are 'Pending':")
    for task in todo_list.list_tasks_by_status("Pending"):
        print(f"- {task}")

def main():
    todo_list = ToDoList()

    # Predefined tasks
    todo_list.add_task("Buy groceries", "Medium")
    todo_list.add_task("Pay bills", "High")
    todo_list.add_task("Walk", "Medium")
    todo_list.add_task("Talk with friends", "High")
    todo_list.add_task("Study", "High")

    # Mark a task as completed
    todo_list.mark_task_pendiente("Buy groceries")
    todo_list.mark_task_completed("Buy groceries")
    todo_list.mark_task_completed("Pay bills")

    # Update priority of a task
    todo_list.update_task_priority("Read a book", "Medium")

    # Print summary
    print_summary(todo_list)

    # Remove a task
    todo_list.remove_task("Buy groceries")
    print("\nTo-Do List after removing 'Buy groceries':")
    print_summary(todo_list)

    # Clear the list
    todo_list.clear_list()
    print("\nTo-Do List after clearing:")
    print_summary(todo_list)

if __name__ == "__main__":
    main()