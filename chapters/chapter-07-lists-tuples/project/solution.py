"""
Chapter 7 Project: To-Do List Manager -- reference solution.
See README.md in this folder for the full brief and example output.

Each task is stored as a small two-item list: [task_text, is_done].
All tasks live together in one master list called `tasks`, so the whole
program is really just list operations -- append, indexing, mutation,
removal, and iteration -- applied to a running collection.
"""

tasks = []  # master list of [task_text, is_done] tasks

print("=== To-Do List Manager ===")

while True:
    print()
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task complete")
    print("4. Remove a task")
    print("5. View session stats")
    print("6. Quit")
    choice = input("Choose an option (1-6): ").strip()

    if choice == "1":
        task_text = input("Enter the new task: ").strip()

        if task_text == "":
            print("A task can't be blank -- nothing was added.")
        else:
            tasks.append([task_text, False])
            print(f"Added: '{task_text}'")

    elif choice == "2":
        print()
        if len(tasks) == 0:
            print("Your to-do list is empty.")
        else:
            print("--- Your Tasks ---")
            for i in range(len(tasks)):
                task_text = tasks[i][0]
                is_done = tasks[i][1]
                status = "x" if is_done else " "
                print(f"{i + 1}. [{status}] {task_text}")

    elif choice == "3":
        if len(tasks) == 0:
            print("Your to-do list is empty -- nothing to mark complete.")
        else:
            raw = input("Enter the task number to mark complete: ").strip()
            if raw.isdigit() and 1 <= int(raw) <= len(tasks):
                index = int(raw) - 1
                tasks[index][1] = True
                print(f"Marked complete: '{tasks[index][0]}'")
            else:
                print(f"Please enter a number between 1 and {len(tasks)}.")

    elif choice == "4":
        if len(tasks) == 0:
            print("Your to-do list is empty -- nothing to remove.")
        else:
            raw = input("Enter the task number to remove: ").strip()
            if raw.isdigit() and 1 <= int(raw) <= len(tasks):
                index = int(raw) - 1
                removed_task = tasks.pop(index)
                print(f"Removed: '{removed_task[0]}'")
            else:
                print(f"Please enter a number between 1 and {len(tasks)}.")

    elif choice == "5":
        total = len(tasks)
        completed = 0
        for task in tasks:
            if task[1]:
                completed += 1
        pending = total - completed

        print()
        print("--- Session Stats ---")
        print(f"Total tasks: {total}")
        print(f"Completed: {completed}")
        print(f"Pending: {pending}")
        if total > 0:
            completion_rate = (completed / total) * 100
            print(f"Completion rate: {completion_rate:.1f}%")
        else:
            print("No tasks yet this session.")

    elif choice == "6":
        total = len(tasks)
        completed = 0
        for task in tasks:
            if task[1]:
                completed += 1
        print()
        print(f"Session summary: {total} task(s) total, {completed} completed.")
        print("Goodbye!")
        break

    else:
        print("Please choose 1-6.")
