import csv
import json
from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date  # string YYYY-MM-DD or None
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date or 'N/A'}, {self.status}"

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["task_id"],
            data["title"],
            data["description"],
            data.get("due_date"),
            data["status"]
        )


# Abstract storage interface
class TaskStorage:
    def save(self, tasks, filename):
        raise NotImplementedError

    def load(self, filename):
        raise NotImplementedError


# CSV Storage implementation
class CSVStorage(TaskStorage):
    def save(self, tasks, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["task_id", "title", "description", "due_date", "status"])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    def load(self, filename):
        tasks = []
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(Task.from_dict(row))
        return tasks


# JSON Storage implementation
class JSONStorage(TaskStorage):
    def save(self, tasks, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)

    def load(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [Task.from_dict(item) for item in data]


# Factory method for storage
def get_storage(format_name):
    format_name = format_name.lower()
    if format_name == 'csv':
        return CSVStorage()
    elif format_name == 'json':
        return JSONStorage()
    else:
        raise ValueError(f"Unsupported storage format: {format_name}")


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if any(t.task_id == task.task_id for t in self.tasks):
            print("Task ID already exists. Use a unique Task ID.")
            return
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
            return
        print("Tasks:")
        for task in self.tasks:
            print(task)

    def update_task(self, task_id, **updates):
        for task in self.tasks:
            if task.task_id == task_id:
                for key, value in updates.items():
                    if hasattr(task, key):
                        setattr(task, key, value)
                print("Task updated successfully!")
                return
        print("Task ID not found.")

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task.task_id == task_id:
                del self.tasks[i]
                print("Task deleted successfully!")
                return
        print("Task ID not found.")

    def filter_tasks(self, status):
        filtered = [task for task in self.tasks if task.status.lower() == status.lower()]
        if not filtered:
            print(f"No tasks with status '{status}'.")
            return
        print(f"Tasks with status '{status}':")
        for task in filtered:
            print(task)

    def save_tasks(self, format_name, filename):
        try:
            storage = get_storage(format_name)
            storage.save(self.tasks, filename)
            print(f"Tasks saved to {filename} in {format_name.upper()} format.")
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self, format_name, filename):
        try:
            storage = get_storage(format_name)
            self.tasks = storage.load(filename)
            print(f"Tasks loaded from {filename} in {format_name.upper()} format.")
        except Exception as e:
            print(f"Error loading tasks: {e}")


def get_task_input():
    task_id = input("Enter Task ID: ").strip()
    title = input("Enter Title: ").strip()
    description = input("Enter Description: ").strip()
    due_date = input("Enter Due Date (YYYY-MM-DD, optional): ").strip()
    if due_date == "":
        due_date = None
    else:
        # Validate date format loosely
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Setting due date to None.")
            due_date = None
    status = input("Enter Status (Pending/In Progress/Completed): ").strip()
    if status not in ["Pending", "In Progress", "Completed"]:
        print("Invalid status. Setting status to 'Pending'.")
        status = "Pending"
    return Task(task_id, title, description, due_date, status)


def main():
    task_manager = TaskManager()
    print("Welcome to the To-Do Application!")

    while True:
        print("""
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit
        """)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            task = get_task_input()
            task_manager.add_task(task)
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_id = input("Enter Task ID to update: ").strip()
            field = input("Enter field to update (title, description, due_date, status): ").strip()
            if field not in ["title", "description", "due_date", "status"]:
                print("Invalid field.")
                continue
            value = input(f"Enter new value for {field}: ").strip()
            if field == "due_date" and value != "":
                try:
                    datetime.strptime(value, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format.")
                    continue
            if field == "status" and value not in ["Pending", "In Progress", "Completed"]:
                print("Invalid status value.")
                continue
            task_manager.update_task(task_id, **{field: value})
        elif choice == "4":
            task_id = input("Enter Task ID to delete: ").strip()
            task_manager.delete_task(task_id)
        elif choice == "5":
            status = input("Enter status to filter by (Pending/In Progress/Completed): ").strip()
            task_manager.filter_tasks(status)
        elif choice == "6":
            format_name = input("Enter format to save (csv/json): ").strip()
            filename = input("Enter filename to save to: ").strip()
            task_manager.save_tasks(format_name, filename)
        elif choice == "7":
            format_name = input("Enter format to load (csv/json): ").strip()
            filename = input("Enter filename to load from: ").strip()
            task_manager.load_tasks(format_name, filename)
        elif choice == "8":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
