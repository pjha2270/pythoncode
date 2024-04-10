# Function to add a task to the todo list 
def add_task(todo_list, task):
    todo_list.append(task)
    print("Task added successfully!")

# Function to view all tasks in the todo list
def view_tasks(todo_list):
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to mark a task as completed
def complete_task(todo_list, task_index):
    if task_index < 1 or task_index > len(todo_list):
        print("Invalid task index.")
    else:
        print(f"Task '{todo_list[task_index - 1]}' marked as completed.")
        todo_list.pop(task_index - 1)

# Function to delete a task from the todo list
def delete_task(todo_list, task_index):
    if task_index < 1 or task_index > len(todo_list):
        print("Invalid task index.")
    else:
        print(f"Task '{todo_list[task_index - 1]}' deleted.")
        todo_list.pop(task_index - 1)

# Main function
def main():
    todo_list = []

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(todo_list, task)
        elif choice == '2':
            view_tasks(todo_list)
        elif choice == '3':
            task_index = int(input("Enter task index to mark as completed: "))
            complete_task(todo_list, task_index)
        elif choice == '4':
            task_index = int(input("Enter task index to delete: "))
            delete_task(todo_list, task_index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
# Making changes to the comment but not the code