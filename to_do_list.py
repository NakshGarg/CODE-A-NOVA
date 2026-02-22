tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    title = input("Enter task name: ")
    tasks.append({"title": title, "status": "Pending"})
    print("✅ Task added successfully!")

def view_tasks():
    if not tasks:
        print("⚠️ No tasks found.")
        return
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']} - {task['status']}")

def update_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to update: "))
        if 1 <= task_no <= len(tasks):
            new_status = input("Enter new status (Pending/Done): ")
            tasks[task_no - 1]["status"] = new_status
            print("🔄 Task updated successfully!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"🗑️ Task '{removed['title']}' deleted.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# -------------------------------
# Main Program Loop
# -------------------------------
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("👋 Exiting To-Do List. Stay productive.")
        break
    else:
        print("❌ Invalid choice. Try again.")
