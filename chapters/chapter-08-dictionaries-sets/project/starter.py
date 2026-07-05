"""
Chapter 8 Project: Inventory Tracker
See README.md in this folder for the full brief and example output.

Inventory is one dictionary mapping item name -> a details dictionary,
e.g. {"quantity": 10, "price": 4.99}. All items live together in one
master dict called `inventory`.
"""

inventory = {}  # master dict: item name -> {"quantity": int, "price": float}
LOW_STOCK_THRESHOLD = 5

print("=== Inventory Tracker ===")

while True:
    print()
    print("1. Add a new item")
    print("2. Update stock quantity")
    print("3. Remove an item")
    print("4. View full inventory")
    print("5. Search for an item")
    print("6. View low-stock report")
    print("7. View total inventory value")
    print("8. Quit")
    choice = input("Choose an option (1-8): ").strip()

    if choice == "1":
        name = input("Enter the item name: ").strip()

        # TODO 1: If name is blank, print a message saying an item name
        # can't be blank and add nothing. If name already exists in
        # `inventory`, print a message telling the user to use option 2
        # instead. Otherwise, ask for a starting quantity and a unit
        # price with input(), check quantity is a whole number
        # (.isdigit()) and price is a number (hint: try
        # price_raw.replace(".", "", 1).isdigit() to allow one decimal
        # point), then store inventory[name] = {"quantity": ..., "price": ...}
        # (converting the strings with int()/float() first) and print a
        # confirmation showing the name, quantity, and price.

    elif choice == "2":
        if len(inventory) == 0:
            print("Inventory is empty -- nothing to update.")
        else:
            name = input("Enter the item name to update: ").strip()
            # TODO 2: If `name` is not in `inventory`, print a message
            # saying it wasn't found. Otherwise ask for a new quantity,
            # validate it's a whole number, and set
            # inventory[name]["quantity"] to the new value. Print a
            # confirmation.
            pass

    elif choice == "3":
        if len(inventory) == 0:
            print("Inventory is empty -- nothing to remove.")
        else:
            name = input("Enter the item name to remove: ").strip()
            # TODO 3: If `name` is in `inventory`, use inventory.pop(name)
            # to remove it and print a confirmation showing the removed
            # item's name and the quantity it had. Otherwise print a
            # message saying it wasn't found.
            pass

    elif choice == "4":
        print()
        # TODO 4: If `inventory` is empty, print "Inventory is empty."
        # Otherwise print a header line "--- Full Inventory ---" then
        # loop over inventory.items() and print each item's name,
        # quantity, price, and line value (quantity * price), nicely
        # formatted/aligned with f-strings.
        pass

    elif choice == "5":
        if len(inventory) == 0:
            print("Inventory is empty -- nothing to search.")
        else:
            name = input("Enter the item name to search for: ").strip()
            # TODO 5: If `name` is in `inventory`, print its quantity and
            # price. Otherwise print a message saying it wasn't found.
            pass

    elif choice == "6":
        print()
        # TODO 6: If `inventory` is empty, print a message saying there's
        # no low-stock report to show. Otherwise print a header line,
        # loop over inventory.items(), and print every item whose
        # quantity is below LOW_STOCK_THRESHOLD along with how many are
        # left. If nothing is low on stock, print a message saying so.
        pass

    elif choice == "7":
        # TODO 7: Loop over inventory.items() with an accumulator
        # variable, summing quantity * price for every item into a
        # running total_value. Print the total across how many items
        # are tracked, formatted to 2 decimal places.
        pass

    elif choice == "8":
        # TODO 8: Compute the same total_value as TODO 7, print a
        # one-line session summary showing how many items were tracked
        # and the total value, print "Goodbye!", then break out of the
        # loop.
        pass

    else:
        print("Please choose 1-8.")
