class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found!")

    def view_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
                print("-----------------")
        else:
            print("Your to-do list is empty!")

    def manage_tasks(self):
        while True:
            print("1. Add a task")
            print("2. Remove a task")
            print("3. View tasks")
            print("4. Quit")
            choice = input("Enter your choice: ")

            if choice == "1":
                task = input("Enter the task: ")
                self.add_task(task)
            elif choice == "2":
                task = input("Enter the task to remove: ")
                self.remove_task(task)
            elif choice == "3":
                self.view_tasks()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


todo = ToDoList()
todo.manage_tasks()
