from expense import Expense
import json


class BudgetManager:

    def __init__(self, filename: str = "data.json", expenses: list[Expense] = None):
        self.filename = filename
        self.expenses = expenses if expenses else []
        self.load_data()

    def load_data(self):
        """Reads JSON file, converts dictionaries back into Expense objects, populates the list."""

        self.expenses = []
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                for expense in data:
                    self.expenses.append(Expense(**expense))
            return None  # Success, no error
        except FileNotFoundError:
            return f"File '{self.filename}' not found. Starting with empty expenses list."

    def save_data(self):
        """Converts all objects in the list to dictionaries and writes them to JSON."""
        try:
            with open(self.filename, "w") as f:
                json.dump([expense.to_dict()
                          for expense in self.expenses], f, indent=4)
            return None  # Success, no error
        except (IOError, PermissionError) as e:
            return f"Error saving data to {self.filename}: {e}"

    def add_expense(self, amount: float, category: str, description: str):
        """Creates a new Expense object, adds to list, and saves immediately."""
        new_expense = Expense(amount, category, description)
        self.expenses.append(new_expense)
        self.save_data()
        return None  # Success, no error

    def get_summary(self):
        """Calculates and returns the total amount spent."""
        return sum(expense.amount for expense in self.expenses)
