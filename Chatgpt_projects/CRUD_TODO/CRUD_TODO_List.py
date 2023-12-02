import os

#Now we try to make some todo lists

tasks = []

def add_task(task):
    tasks.append(task)
    save_tasks()

def show_tasks():
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def save_tasks():
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the absolute directory of the script
    file_path = os.path.join(script_dir, "todolist.txt")

    with open(file_path, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")




def main():
    while True:
        print("\n=== To-Do List ===")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            new_task = input("Enter the task: ")
            add_task(new_task)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()