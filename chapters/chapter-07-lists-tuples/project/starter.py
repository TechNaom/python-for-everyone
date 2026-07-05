"""
Chapter 7 Project: To-Do List Manager
See README.md in this folder for the full brief and example output.

Each task is stored as a small two-item list: [task_text, is_done].
All tasks live together in one master list called `tasks`.
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

        # TODO 1: If task_text is an empty string, print a message saying
        # a task can't be blank and add nothing. Otherwise, append a new
        # [task_text, False] list onto `tasks` and print a confirmation
        # line: Added: '<task_text>'

    elif choice == "2":
        print()
        # TODO 2: If `tasks` is empty, print "Your to-do list is empty."
        # Otherwise, print "--- Your Tasks ---" then loop over every
        # index in range(len(tasks)) and print a numbered line for each
        # task in the form:
        #   1. [x] Buy milk        (done tasks show "x")
        #   2. [ ] Walk dog        (pending tasks show a blank space)
        # Remember the displayed number is index + 1, since tasks are
        # stored starting at index 0.

    elif choice == "3":
        # TODO 3: If `tasks` is empty, print a message saying there's
        # nothing to mark complete. Otherwise, ask the user for a task
        # number with input(), check it's a digit string AND within
        # range (1 to len(tasks)), then set that task's is_done flag
        # (tasks[index][1]) to True and print a confirmation showing
        # the task's text. If the number is invalid, print a message
        # telling the user the valid range.
        pass

    elif choice == "4":
        # TODO 4: Same validation pattern as TODO 3, but instead of
        # marking complete, use tasks.pop(index) to remove that task
        # from the list entirely. Print a confirmation showing the
        # removed task's text.
        pass

    elif choice == "5":
        # TODO 5: Compute total = len(tasks). Loop over `tasks` and
        # count how many have is_done == True into a variable called
        # completed. Compute pending = total - completed. Print all
        # three. If total > 0, also print the completion rate as a
        # percentage (completed / total * 100) formatted to 1 decimal
        # place. Otherwise print a message saying there are no tasks yet.
        pass

    elif choice == "6":
        # TODO 6: Compute the same total/completed counts as TODO 5,
        # print a one-line session summary showing both, print
        # "Goodbye!", then break out of the loop.
        pass

    else:
        print("Please choose 1-6.")
