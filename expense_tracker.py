import os

FILE_NAME = "expenses.txt"

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food/Travel/Education/etc): ")
    
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    description = input("Enter description (optional): ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{category},{amount},{description}\n")

    print("Expense added successfully!\n")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.\n")
        return

    print("\nDate\t\tCategory\tAmount\tDescription")
    print("-" * 60)

    with open(FILE_NAME, "r") as file:
        for line in file:
            date, category, amount, description = line.strip().split(",")
            print(f"{date}\t{category}\t{amount}\t{description}")

    print()


def total_expense():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.\n")
        return

    total = 0
    with open(FILE_NAME, "r") as file:
        for line in file:
            data = line.strip().split(",")
            total += float(data[2])

    print(f"Total Expense: ₹{total}\n")


def category_wise_expense():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.\n")
        return

    categories = {}

    with open(FILE_NAME, "r") as file:
        for line in file:
            _, category, amount, _ = line.strip().split(",")
            amount = float(amount)

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    print("\nCategory-wise Expenses:")
    for category, amount in categories.items():
        print(f"{category}: ₹{amount}")
    print()


def main():
    while True:
        print("===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expense")
        print("4. Category-wise Expense")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            category_wise_expense()
        elif choice == "5":
            print("Exiting Expense Tracker. Stay financially smart.")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
