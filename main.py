
def display_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list):
            print(f"{index + 1}. {task}")


def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")


def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task index. Please enter a valid index.")



def main():
    todo_list = []  # Initialize an empty to-do list

    while True:
        # Display menu
        print("\nMenu:")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")


        choice = input("Enter your choice: ")

        if choice == '1':
            display_list(todo_list)
        elif choice == '2':
            task = input("Enter the task to add: ")
            add_task(todo_list, task)
        elif choice == '3':
            task_index = int(input("Enter the task index to remove: "))
            remove_task(todo_list, task_index)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")



if __name__ == "__main__":
    main()
