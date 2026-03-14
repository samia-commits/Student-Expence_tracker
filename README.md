# Student Expense Tracker

A simple command-line app to help students track daily expenses, manage budgets, and view spending summaries.

## Features

- Add expenses with category, amount, and description
- View all expenses in a clean table
- Delete expenses by ID
- Filter expenses by category or date
- View spending summary per category
- Set a monthly budget and track remaining balance

## Project Structure

```
student-expense-tracker/
├── main.py          # CLI entry point
├── expenses.py      # Core expense logic
├── storage.py       # JSON data persistence
├── requirements.txt # Dependencies
└── data.json        # Auto-generated data file
```

## Setup

1. Clone the repo

```bash
git clone https://github.com/samia-commits/Student-Expence_tracker.git
cd Student-Expence_tracker
```

2. (Optional) Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the app

```bash
python main.py
```

## Usage

Once running, you'll see a menu:

```
=== Student Expense Tracker ===
1. Add expense
2. View all expenses
3. Delete expense
4. View summary by category
5. Filter by category
6. Filter by date
7. Set budget
8. View total & budget status
0. Exit
```

## Categories

`Food`, `Transport`, `Books`, `Entertainment`, `Health`, `Rent`, `Other`

## Requirements

- Python 3.7+
- tabulate
- colorama
