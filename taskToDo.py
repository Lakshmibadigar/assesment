class Task:         # created a class called task
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date): # function to add task
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_completed(self, task_index):  #function to mark the completed task
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True

    def delete_task(self, task_index):          #function to delete the task 
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]

    def view_tasks(self, filter_completed=False):       # viewing the tasks
        if filter_completed:
            tasks_to_display = [task for task in self.tasks if task.completed] #for displaying the completed tasks
        else:
            tasks_to_display = [task for task in self.tasks if not task.completed]      # for displaying the pending tasks

        for i, task in enumerate(tasks_to_display):
            status = "Completed" if task.completed else "Pending"
            print(f"{i + 1}. Description : {task.description}, Due Date: {task.due_date}, Status: {status}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Add The Task--")
        print("2. Mark Task as Completed--")
        print("3. Delete Task--")
        print("4. View Tasks--")
        print("5. View Completed Tasks--")
        print("6. view Pending Tasks")
        print("7. quit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            todo_list.add_task(description, due_date)
        elif choice == "2":
            index = int(input("Enter the index of the task to mark as completed: "))
            todo_list.mark_task_completed(index - 1)
        elif choice == "3":
            index = int(input("Enter the index of the task to delete: "))
            todo_list.delete_task(index - 1)
        elif choice == "4":
            todo_list.view_tasks()
        elif choice == "5":
            todo_list.view_tasks(filter_completed=True)
        elif choice == "6":
            todo_list.view_tasks(filter_completed=False)
        elif choice=="7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
