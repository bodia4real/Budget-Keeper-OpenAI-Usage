from budgetkeeper import BudgetManager
from agent import parse_expense


def main():
    manager = BudgetManager()

    print("Welcome to BudgetKeeper!")

    while True:
        print("\n--- MENU ---")
        print("1. Add Expense")
        print("2. Add Expense with AI")
        print("3. View Expenses")
        print("4. Show Total")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            while True:
                amount = input("Enter the amount: ")
                try:
                    amount = float(amount)
                    break
                except ValueError:
                    print("Invalid amount, please enter a valid number.")

            category = input("Enter the category: ")
            description = input("Enter the description: ")

            manager.add_expense(amount, category, description)
            print("Expense added successfully.")

        elif choice == '2':
            user_text = input("Enter the expense: ")
            print("Thinking...")
            expense_data = parse_expense(user_text)
            if expense_data and expense_data['amount'] > 0:
                manager.add_expense(
                    amount=expense_data['amount'], category=expense_data['category'], description=expense_data['description'])
                print(
                    f"Success! Added ${expense_data['amount']} for {expense_data['category']}.")
            else:
                print("Failed to parse expense.")

        elif choice == '3':
            print("\n--- Your Expenses ---")
            for expense in manager.expenses:
                print(
                    f"Amount: {expense.amount}, Category: {expense.category}, Description: {expense.description}, Date: {expense.date}")
            if not manager.expenses:
                print("No expenses found.")

        elif choice == '4':
            print("\n--- Total Spent ---")
            print(manager.get_summary())

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
