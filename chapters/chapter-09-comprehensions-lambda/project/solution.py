"""
Chapter 9 Project: Data-Cleaning One-Liners Kit -- reference solution.
See README.md in this folder for the full brief and example output.

raw_records is a list of dicts -- messy, inconsistent data straight off a
form or a spreadsheet export (extra whitespace, mixed case, some blank or
invalid fields). cleaned_records holds the result after running it through
comprehensions, lambda, map, filter, and sorted -- this chapter's core
tools -- instead of hand-written loops with .append().
"""

raw_records = [
    {"name": "  Ana Silva ", "email": "ANA@Example.com", "age": "29"},
    {"name": "bruno costa", "email": "  bruno@example.com", "age": "34"},
    {"name": "  ", "email": "no-name@example.com", "age": "22"},
    {"name": "Carla Dias", "email": "", "age": "41"},
    {"name": "DANIEL ROCHA", "email": "daniel@EXAMPLE.com  ", "age": "abc"},
    {"name": "elena Ferreira", "email": "elena@example.com", "age": "27"},
    {"name": "Felipe Souza", "email": "felipe@example.com", "age": "-5"},
    {"name": "  Gabriela Nunes", "email": "gabriela@example.com", "age": "31"},
]

cleaned_records = []  # populated by option 2

print("=== Data-Cleaning One-Liners Kit ===")

while True:
    print()
    print("1. Show raw sample data")
    print("2. Clean whitespace & casing")
    print("3. Filter out invalid records")
    print("4. Sort cleaned data by a field")
    print("5. Generate a summary report")
    print("6. Export final cleaned dataset")
    print("7. Quit")
    choice = input("Choose an option (1-7): ").strip()

    if choice == "1":
        print()
        print("--- Raw Sample Data ---")
        for record in raw_records:
            print(record)

    elif choice == "2":
        # A comprehension rebuilds every record with each field's
        # whitespace stripped and casing normalized -- this is the
        # idiomatic replacement for a for-loop + .append() here.
        cleaned_records = [
            {
                "name": record["name"].strip().title(),
                "email": record["email"].strip().lower(),
                "age": record["age"].strip(),
            }
            for record in raw_records
        ]
        print()
        print(f"Cleaned {len(cleaned_records)} record(s) -- whitespace stripped, names title-cased, emails lowercased.")

    elif choice == "3":
        if len(cleaned_records) == 0:
            print("No cleaned data yet -- run option 2 first.")
        else:
            before_count = len(cleaned_records)
            # filter() + lambda drops any record with a blank name, a
            # blank email, or a non-numeric/non-positive age -- exactly
            # the kind of one-off predicate lambda is built for.
            cleaned_records = list(filter(
                lambda r: r["name"] != "" and r["email"] != "" and r["age"].isdigit() and int(r["age"]) > 0,
                cleaned_records
            ))
            removed = before_count - len(cleaned_records)
            print()
            print(f"Removed {removed} invalid record(s) -- {len(cleaned_records)} record(s) remain.")

    elif choice == "4":
        if len(cleaned_records) == 0:
            print("No cleaned data yet -- run options 2 and 3 first.")
        else:
            print()
            print("Sort by: 1) name  2) email  3) age")
            field_choice = input("Choose a field (1-3): ").strip()

            if field_choice == "1":
                cleaned_records = sorted(cleaned_records, key=lambda r: r["name"])
                print("Sorted by name.")
            elif field_choice == "2":
                cleaned_records = sorted(cleaned_records, key=lambda r: r["email"])
                print("Sorted by email.")
            elif field_choice == "3":
                cleaned_records = sorted(cleaned_records, key=lambda r: int(r["age"]))
                print("Sorted by age.")
            else:
                print("Please choose 1-3.")

            print()
            for record in cleaned_records:
                print(record)

    elif choice == "5":
        print()
        if len(cleaned_records) == 0:
            print("No cleaned data yet -- run option 2 first.")
        else:
            # A comprehension collects every age as an int for the
            # average, and a dict comprehension buckets records by an
            # age-group label -- both natural fits for this chapter.
            ages = [int(r["age"]) for r in cleaned_records]
            average_age = sum(ages) / len(ages)

            age_groups = {"under 30": 0, "30-39": 0, "40 and up": 0}
            for age in ages:
                if age < 30:
                    age_groups["under 30"] += 1
                elif age < 40:
                    age_groups["30-39"] += 1
                else:
                    age_groups["40 and up"] += 1

            domain_counts = {}
            domains = [r["email"].split("@")[-1] for r in cleaned_records if "@" in r["email"]]
            for domain in domains:
                domain_counts[domain] = domain_counts.get(domain, 0) + 1

            print("--- Summary Report ---")
            print(f"Total cleaned records: {len(cleaned_records)}")
            print(f"Average age: {average_age:.1f}")
            print(f"Age groups: {age_groups}")
            print(f"Records per email domain: {domain_counts}")

    elif choice == "6":
        print()
        if len(cleaned_records) == 0:
            print("No cleaned data yet -- nothing to export.")
        else:
            print("--- Final Cleaned Dataset ---")
            print(f"{'Name':<20}{'Email':<28}{'Age':<6}")
            for record in cleaned_records:
                print(f"{record['name']:<20}{record['email']:<28}{record['age']:<6}")

    elif choice == "7":
        print()
        print(f"Session summary: {len(cleaned_records)} cleaned record(s) ready for export.")
        print("Goodbye!")
        break

    else:
        print("Please choose 1-7.")
