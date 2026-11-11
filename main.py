
import json
from pathlib import Path
from datetime import date


DATA_FILE = Path(__file__).with_name("expenses.json")


def load_expenses():
    """Load saved expenses from the JSON file."""

    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            expenses = json.load(file)

        if isinstance(expenses, list):
            return expenses

        print("Warning: The saved expense data has an unexpected format.")
        return []

    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read the saved expenses.")
        return []


def save_expenses(expenses):
    """Save all expenses to the JSON file."""

    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)

        return True

    except OSError:
        print("Error: Your expenses could not be saved.")
        return False


def get_amount():
    """Ask the user for a valid positive expense amount."""

    while True:
        try:
            amount = float(input("How much did it cost? £"))

            if amount <= 0:
                print("Please enter an amount greater than zero.")
            else:
                return round(amount, 2)

        except ValueError:
            print("Please enter a valid number, such as 4.50.")


def add_expense(expenses):
    """Collect and save a new expense."""

    print("\n--- Add an Expense ---")

    description = input("What did you buy? ").strip()

    if not description:
        print("Description cannot be empty.")
        return

    amount = get_amount()

    category = input("What category does it belong to? ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    expense = {
        "description": description,
        "amount": amount,
        "category": category.title(),
        "date": date.today().isoformat()
    }

    expenses.append(expense)

    if save_expenses(expenses):
        print("\nExpense added successfully!")
        print(f"Description: {description}")
        print(f"Amount: £{amount:.2f}")
        print(f"Category: {category.title()}")
    else:
        expenses.pop()


def view_expenses(expenses):
    """Display all saved expenses."""

    print("\n--- All Expenses ---")

    if not expenses:
        print("You haven't recorded any expenses yet.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(f"\nExpense {number}")
        print(f"Date: {expense.get('date', 'Unknown')}")
        print(f"Description: {expense['description']}")
        print(f"Amount: £{expense['amount']:.2f}")
        print(f"Category: {expense['category']}")

    print("\n-------------------------")
    print(f"Number of expenses: {len(expenses)}")


def spending_summary(expenses):
    """Calculate total spending and spending by category."""

    print("\n--- Spending Summary ---")

    if not expenses:
        print("No expenses available to calculate.")
        return

    total = sum(expense["amount"] for expense in expenses)

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print(f"\nTotal spending: £{total:.2f}")
    print(f"Number of expenses: {len(expenses)}")
    print(f"Average expense: £{total / len(expenses):.2f}")

    print("\nSpending by category:")

    for category, amount in category_totals.items():
        print(f"{category}: £{amount:.2f}")


def display_menu():
    """Display the main menu."""

    print("\n==============================")
    print("     PERSONAL EXPENSE TRACKER")
    print("==============================")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View spending summary")
    print("4. Exit")
    print("==============================")


def main():
    """Run the expense tracker application."""

    expenses = load_expenses()

    print("Welcome to your Personal Expense Tracker!")

    while True:
        display_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            spending_summary(expenses)

        elif choice == "4":
            print("\nThank you for using the Expense Tracker!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid option. Please choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()

