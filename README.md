# 💰 BudgetKeeper CLI - Project Plan

**Goal:** Build a persistent Command Line Interface (CLI) expense tracker to master Python OOP, File I/O, and Modular Architecture.

---

## 📂 Project Structure (Architecture)

You are building a modular application with 3 separate files.

| File Name         | Role            | Analogy        | Imports Needed                               |
| ----------------- | --------------- | -------------- | -------------------------------------------- |
| `expense.py`      | Data Model      | The Receipt    | None                                         |
| `budgetkeeper.py` | Manager / Logic | The Accountant | `from expense import Expense`, `import json` |
| `main.py`         | User Interface  | The Counter    | `from budgetkeeper import BudgetManager`     |

---

## 🛠️ Implementation Steps

### Step 1: expense.py (The Foundation)

This class defines what an "Expense" actually is.

**Class Name:** `Expense`

**Attributes (in `__init__`):**

- `amount` (float)
- `category` (string)
- `description` (string)
- `date` (string - optional, use `datetime.now()` if you want to be fancy)

**Methods:**

- `to_dict(self)`: Returns a dictionary representation of the object (e.g., `{"amount": 50, ...}`). Crucial for saving to JSON later.

---

### Step 2: budgetkeeper.py (The Brains)

This class manages the list of expenses and talks to the hard drive.

**Class Name:** `BudgetManager`

**Attributes:**

- `filename`: The name of the save file (e.g., `"data.json"`).
- `expenses`: A list `[]` that holds Expense objects.

**Methods:**

- `load_data()`: Reads JSON file, converts dictionaries back into Expense objects, populates the list.
- `save_data()`: Converts all objects in the list to dictionaries and writes them to JSON.
- `add_expense(amount, category, description)`: Creates a new Expense object, adds to list, and saves immediately.
- `get_summary()`: Logic to calculate total spent.

---

### Step 3: main.py (The Loop)

The interface that runs forever until the user quits.

**Logic:**

1. Instantiate `manager = BudgetManager()` (This should trigger a load of old data).
2. Start `while True:` loop.
3. Print Menu: `[1] Add Expense [2] View Summary [3] Quit`.
4. Get user input.
5. Call the corresponding method in manager.

**Safety:** Use try/except blocks here so if the user types "ABC" instead of a price, the app doesn't crash.

---

## 📋 Requirements Checklist

### Functional

- [ ] **Persistence:** If I close the terminal and re-open it, my past expenses must still be there.
- [ ] **Categorization:** I must be able to categorize an item (e.g., "Food", "Transport").
- [ ] **Summary:** I must be able to see the total money spent.

### Technical (The "Test")

- [ ] **OOP:** Use Classes (no global lists).
- [ ] **File I/O:** Use json library to read/write `data.json`.
- [ ] **Type Conversion:** Handle converting strings (from JSON) back to Objects (for Python).
- [ ] **Error Handling:** App handles missing files (first run) and bad inputs.
