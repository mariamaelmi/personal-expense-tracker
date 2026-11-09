

while True:
    print("\nPERSONAL EXPENSE TRACKER")
    print("========================")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View spending summary")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Add an expense selected!")
    elif choice == "2":
        print("View all expenses selected!")
    elif choice == "3":
        print("View spending summary selected!")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
