import json
import csv
tasks = """[
    {"id": 1, "task": "Do laundry", "completed": false, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": true, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": false, "priority": 1}
]
"""
task_data = json.loads(tasks)
with open("tasks.json", "w") as file:
    json.dump(task_data, file, indent = 4)

with open("tasks.json", "r") as file:
    tasks = json.load(file)
print("All Tasks:\n")
for task in tasks:
    print(f"ID: {task['id']}")
    print(f"Task Name: {task['task']}")
    print(f"Completed: {task['completed']}")
    print(f"Priority: {task['priority']}")
    print("-" * 25)

for task in tasks:
        if task["id"] == 1:
            task["completed"] = True
print("\nTasks after modification:\n")
for task in tasks:
    print(f"ID: {task['id']}")
    print(f"Task Name: {task['task']}")
    print(f"Completed: {task['completed']}")
    print(f"Priority: {task['priority']}")
    print("-" * 25)

with open("tasks.json", "w") as file:
    json.dump(tasks, file, indent = 4)
print("\nChanges saved successfully")

def text_completion_stats():
    count_tasks = 0
    count_completed_tasks = 0
    count_pending_tasks = 0
    priority_sum = 0

    for task in tasks:
        count_tasks += 1
        if task["completed"]:
            count_completed_tasks += 1
        else:
            count_pending_tasks += 1
        priority_sum += task["priority"]

    average_priority = priority_sum / count_tasks if count_tasks else 0
    print(f"\nTotal tasks: {count_tasks}")
    print(f"Completed tasks: {count_completed_tasks}")
    print(f"Pending tasks: {count_pending_tasks}")
    print(f"Average Priority: {average_priority}")
text_completion_stats()

def json_to_csv(json_filename, csv_filename):
     with open(json_filename, "r") as file:
          tasks = json.load(file)
     with open(csv_filename, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerow(['ID', 'Task', 'Completed', 'Priority'])
          for task in tasks:
                writer.writerow([
                task['id'],
                task['task'],
                task['completed'],
                task['priority']
            ])
json_to_csv('tasks.json', 'tasks.csv')