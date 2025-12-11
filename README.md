# 💰 BudgetKeeper CLI

A smart command-line expense tracker with AI-powered natural language parsing, built with Python OOP principles.

## ✨ Features

- **📝 Manual Expense Entry**: Add expenses with amount, category, and description
- **🤖 AI-Powered Entry**: Simply describe your expense in natural language - the AI extracts the details automatically
- **📊 Expense Viewing**: View all your expenses with full details
- **💰 Spending Summary**: Calculate your total spending at a glance
- **💾 Persistent Storage**: All expenses are saved to JSON and persist across sessions
- **🗓️ Auto-Dated**: Expenses are automatically timestamped

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- OpenAI API key

### Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd "Budget Keeper"
```

2. Install required dependencies:

```bash
pip install openai python-dotenv
```

3. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

### Running the Application

```bash
python main.py
```

## 📖 Usage

When you run the application, you'll see a menu with the following options:

```
--- MENU ---
1. Add Expense
2. Add Expense with AI
3. View Expenses
4. Show Total
5. Exit
```

### Option 1: Manual Expense Entry

Enter the expense details manually:

- **Amount**: The expense amount (e.g., `25.50`)
- **Category**: A category name (e.g., `Food`, `Transport`, `Bills`)
- **Description**: A brief description of the expense

### Option 2: AI-Powered Expense Entry ⚡

Simply describe your expense in natural language! The AI will automatically extract the amount, category, and description.

**Examples:**

- `"I spent $15.50 on lunch at McDonald's"`
- `"Uber ride to airport cost me 45 dollars"`
- `"Paid 120 for monthly internet bill"`
- `"Bought groceries for 87.99 today"`

The AI intelligently:

- Extracts the amount from various formats
- Categorizes the expense (Food, Transport, Bills, Entertainment, etc.)
- Creates a concise description

### Option 3: View Expenses

Displays all your expenses with:

- Amount
- Category
- Description
- Date

### Option 4: Show Total

Calculates and displays your total spending across all expenses.

## 📂 Project Structure

```
Budget Keeper/
│
├── expense.py          # Expense data model class
├── budgetkeeper.py     # BudgetManager class (CRUD & persistence)
├── main.py            # CLI interface and main menu
├── agent.py           # AI integration for natural language parsing
├── data.json          # Persistent storage (created automatically)
├── .env               # Environment variables (API key)
└── README.md          # This file
```

### Architecture

- **`expense.py`**: The `Expense` class - data model representing a single expense
- **`budgetkeeper.py`**: The `BudgetManager` class - handles expense management and JSON persistence
- **`main.py`**: User interface with interactive menu loop
- **`agent.py`**: AI integration using OpenAI API to parse natural language expenses

## 🛠️ Technical Details

### Design Patterns

- **Object-Oriented Design**: Clean separation using classes (Expense, BudgetManager)
- **Separation of Concerns**: Model (Expense), Manager (BudgetManager), UI (main.py), AI (agent.py)
- **Error Handling**: Graceful handling of missing files, invalid inputs, and API errors

### Data Storage

- Expenses are stored in `data.json` in JSON format
- Data persists across sessions automatically
- First run creates an empty `data.json` file

### AI Integration

- Uses OpenAI's GPT model for natural language processing
- Extracts structured data (amount, category, description) from unstructured text
- Returns JSON format for reliable parsing

## 📋 Requirements Checklist

### Functional ✅

- ✅ **Persistence**: Expenses persist across terminal sessions
- ✅ **Categorization**: Expenses can be categorized
- ✅ **Summary**: Total spending calculation available
- ✅ **AI Parsing**: Natural language expense entry

### Technical ✅

- ✅ **OOP**: Object-oriented design with classes
- ✅ **File I/O**: JSON-based persistent storage
- ✅ **Type Conversion**: JSON ↔ Python object conversion
- ✅ **Error Handling**: Robust error handling for files and inputs

## 🔧 Configuration

### OpenAI Model

The AI feature uses GPT-5-nano by default. You can modify the model in `agent.py`:

```python
model = "gpt-5-nano"  # Change to your preferred model
```

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements!

## 📝 License

This project is open source and available for personal use.

## 💡 Example Session

```
Welcome to BudgetKeeper!

--- MENU ---
1. Add Expense
2. Add Expense with AI
3. View Expenses
4. Show Total
5. Exit
Enter your choice (1-5): 2

Enter the expense: Spent 45 dollars on groceries at Whole Foods
Thinking...
Success! Added $45.0 for Food.

--- MENU ---
1. Add Expense
2. Add Expense with AI
3. View Expenses
4. Show Total
5. Exit
Enter your choice (1-5): 4

--- Total Spent ---
45.0

--- MENU ---
1. Add Expense
2. Add Expense with AI
3. View Expenses
4. Show Total
5. Exit
Enter your choice (1-5): 3

--- Your Expenses ---
Amount: 45.0, Category: Food, Description: groceries at Whole Foods, Date: 2024-01-15
```

---

**Enjoy tracking your expenses with ease!** 💰✨
