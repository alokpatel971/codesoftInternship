import datetime

class Task:
    def __init__(self, title, due_date=None):
        self.title = title
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, due_date=None):
        task = Task(title, due_date)
        self.tasks.append(task)

    def view_tasks(self):
        print("Your To-Do List:")
        for index, task in enumerate(self.tasks):
            status = "Completed" if task.completed else "Incomplete"
            print(f"{index + 1}. {task.title} - Due: {task.due_date} - Status: {status}")

    def update_task(self, task_index, new_title, new_due_date=None):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.title = new_title
            task.due_date = new_due_date
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

def main():
    to_do_list = ToDoList()

    while True:
        print("\n")
        print("To-Do List Options:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Update a task")
        print("4. Mark task as completed")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            if due_date:
                due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
            to_do_list.add_task(title, due_date)
        elif choice == 2:
            to_do_list.view_tasks()
        elif choice == 3:
            task_index = int(input("Enter task index to update: ")) - 1
            new_title = input("Enter new title: ")
            new_due_date = input("Enter new due date (YYYY-MM-DD): ")
            if new_due_date:
                new_due_date = datetime.datetime.strptime(new_due_date, "%Y-%m-%d")
            to_do_list.update_task(task_index, new_title, new_due_date)
        elif choice == 4:
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            to_do_list.mark_task_completed(task_index)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()