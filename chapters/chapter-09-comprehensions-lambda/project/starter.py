"""
Chapter 9 Project: Data-Cleaning One-Liners Kit
See README.md in this folder for the full brief and example output.

raw_records is a list of dicts -- messy, inconsistent data straight off a
form or a spreadsheet export (extra whitespace, mixed case, some blank or
invalid fields). Build cleaned_records by running raw_records through
comprehensions, lambda, map, filter, and sorted -- this chapter's tools --
instead of hand-written loops with .append().
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
        # TODO 1: Print a header "--- Raw Sample Data ---" then loop
        # over raw_records and print each record.
        pass

    elif choice == "2":
        # TODO 2: Use a list comprehension to build cleaned_records --
        # one new dict per record in raw_records, with "name" stripped
        # and .title()-cased, "email" stripped and .lower()-cased, and
        # "age" just stripped. Print a confirmation showing how many
        # records were cleaned.
        pass

    elif choice == "3":
        if len(cleaned_records) == 0:
            print("No cleaned data yet -- run option 2 first.")
        else:
            before_count = len(cleaned_records)
            # TODO 3: Use filter() with a lambda to keep only records
            # where name != "", email != "", age.isdigit(), and
            # int(age) > 0. Wrap the filter() call in list(...) and
            # reassign it to cleaned_records. Print how many records
            # were removed and how many remain.
            pass

    elif choice == "4":
        if len(cleaned_records) == 0:
            print("No cleaned data yet -- run options 2 and 3 first.")
        else:
            print()
            print("Sort by: 1) name  2) email  3) age")
            field_choice = input("Choose a field (1-3): ").strip()

            # TODO 4: Based on field_choice, reassign cleaned_records to
            # sorted(cleaned_records, key=lambda r: ...) using the right
            # field for each choice (age should sort numerically, so
            # convert it with int() inside the lambda). Print which
            # field was used, then loop over cleaned_records and print
            # each record.
            pass

    elif choice == "5":
        print()
        if len(cleaned_records) == 0:
            print("No cleaned data yet -- run option 2 first.")
        else:
            # TODO 5: Build a list of ages (as ints) from cleaned_records
            # using a comprehension, and compute their average. Then
            # build an age_groups dict with keys "under 30", "30-39",
            # "40 and up" counting how many ages fall in each bucket.
            # Then build a domain_counts dict mapping each email's
            # domain (the part after "@") to how many records use it.
            # Print all of it as a summary report.
            pass

    elif choice == "6":
        print()
        if len(cleaned_records) == 0:
            print("No cleaned data yet -- nothing to export.")
        else:
            # TODO 6: Print a header line and column headers for Name,
            # Email, Age, then loop over cleaned_records and print each
            # one aligned into columns with f-strings.
            pass

    elif choice == "7":
        print()
        # TODO 7: Print a one-line session summary showing how many
        # cleaned records are ready for export, print "Goodbye!", then
        # break out of the loop.
        pass

    else:
        print("Please choose 1-7.")
