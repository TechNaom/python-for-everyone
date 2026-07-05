"""
Chapter 8 Project: Inventory Tracker -- reference solution.
See README.md in this folder for the full brief and example output.

Inventory is one dictionary mapping item name -> a details dictionary,
e.g. {"quantity": 10, "price": 4.99}. The whole program is really just
dict operations -- adding keys, looking up nested values, looping with
.items(), and updating fields in place -- applied to a running dict of
records.
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

        if name == "":
            print("An item name can't be blank -- nothing was added.")
        elif name in inventory:
            print(f"'{name}' already exists in inventory -- use option 2 to update its quantity.")
        else:
            qty_raw = input("Enter starting quantity: ").strip()
            price_raw = input("Enter unit price: ").strip()

            if qty_raw.isdigit() and price_raw.replace(".", "", 1).isdigit():
                inventory[name] = {"quantity": int(qty_raw), "price": float(price_raw)}
                print(f"Added: '{name}' (qty {int(qty_raw)}, price ${float(price_raw):.2f})")
            else:
                print("Quantity must be a whole number and price must be a number -- nothing was added.")

    elif choice == "2":
        if len(inventory) == 0:
            print("Inventory is empty -- nothing to update.")
        else:
            name = input("Enter the item name to update: ").strip()
            if name not in inventory:
                print(f"'{name}' was not found in inventory.")
            else:
                qty_raw = input("Enter the new quantity: ").strip()
                if qty_raw.isdigit():
                    inventory[name]["quantity"] = int(qty_raw)
                    print(f"Updated '{name}' to quantity {int(qty_raw)}.")
                else:
                    print("Quantity must be a whole number -- nothing was updated.")

    elif choice == "3":
        if len(inventory) == 0:
            print("Inventory is empty -- nothing to remove.")
        else:
            name = input("Enter the item name to remove: ").strip()
            if name in inventory:
                removed = inventory.pop(name)
                print(f"Removed: '{name}' (had qty {removed['quantity']}).")
            else:
                print(f"'{name}' was not found in inventory.")

    elif choice == "4":
        print()
        if len(inventory) == 0:
            print("Inventory is empty.")
        else:
            print("--- Full Inventory ---")
            print(f"{'Item':<20}{'Quantity':<12}{'Price':<10}{'Line Value':<12}")
            for item_name, details in inventory.items():
                quantity = details["quantity"]
                price = details["price"]
                line_value = quantity * price
                print(f"{item_name:<20}{quantity:<12}${price:<9.2f}${line_value:<11.2f}")

    elif choice == "5":
        if len(inventory) == 0:
            print("Inventory is empty -- nothing to search.")
        else:
            name = input("Enter the item name to search for: ").strip()
            if name in inventory:
                details = inventory[name]
                print(f"'{name}': quantity={details['quantity']}, price=${details['price']:.2f}")
            else:
                print(f"'{name}' was not found in inventory.")

    elif choice == "6":
        print()
        if len(inventory) == 0:
            print("Inventory is empty -- no low-stock report to show.")
        else:
            print(f"--- Low-Stock Report (below {LOW_STOCK_THRESHOLD} units) ---")
            low_stock_count = 0
            for item_name, details in inventory.items():
                if details["quantity"] < LOW_STOCK_THRESHOLD:
                    print(f"{item_name}: only {details['quantity']} left")
                    low_stock_count += 1
            if low_stock_count == 0:
                print("No items are currently low on stock.")

    elif choice == "7":
        total_value = 0
        for item_name, details in inventory.items():
            total_value += details["quantity"] * details["price"]
        print()
        print(f"Total inventory value across {len(inventory)} item(s): ${total_value:.2f}")

    elif choice == "8":
        total_value = 0
        for item_name, details in inventory.items():
            total_value += details["quantity"] * details["price"]
        print()
        print(f"Session summary: {len(inventory)} item(s) tracked, total value ${total_value:.2f}.")
        print("Goodbye!")
        break

    else:
        print("Please choose 1-8.")
