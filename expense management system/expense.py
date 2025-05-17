import os

# File to store expenses
EXPENSE_FILE = "expenses.txt"

# Function to add an expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport, Entertainment): ")
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    with open(EXPENSE_FILE, "a") as file:
        file.write(f"{date},{category},{amount}\n")
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses():
    if not os.path.exists(EXPENSE_FILE):
        print("No expenses recorded yet.")
        return

    print("\nDate       | Category       | Amount")
    print("-------------------------------------")
    with open(EXPENSE_FILE, "r") as file:
        for line in file:
            try:
                date, category, amount = line.strip().split(",")
                print(f"{date} | {category:<13} | {float(amount):.2f}")
            except ValueError:
                continue  # Skip lines that are not properly formatted

# Function to generate a monthly report
def generate_report():
    if not os.path.exists(EXPENSE_FILE):
        print("No expenses recorded yet.")
        return

    month = input("Enter the month to generate the report for (YYYY-MM): ")
    total_expenses = 0
    category_totals = {}

    with open(EXPENSE_FILE, "r") as file:
        for line in file:
            try:
                date, category, amount = line.strip().split(",")
                if date.startswith(month):
                    amount = float(amount)
                    total_expenses += amount
                    category_totals[category] = category_totals.get(category, 0) + amount
            except ValueError:
                continue  # skip malformed lines

    print(f"\nMonthly Report for {month}")
    print(f"Total Expenses: {total_expenses:.2f}")
    print("Category-wise breakdown:")
    for category, total in category_totals.items():
        print(f"{category}: {total:.2f}")

# Main menu
def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Monthly Report")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            generate_report()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Make sure entry point is correct
if __name__ == "__main__":
    main()
