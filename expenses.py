from datetime import datetime

CATEGORIES = ["Food", "Transport", "Books", "Entertainment", "Health", "Rent", "Other"]

def add_expense(data, amount, category, description):
    expense = {
        "id": len(data["expenses"]) + 1,
        "amount": float(amount),
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    data["expenses"].append(expense)
    return expense

def delete_expense(data, expense_id):
    original = len(data["expenses"])
    data["expenses"] = [e for e in data["expenses"] if e["id"] != expense_id]
    return len(data["expenses"]) < original

def get_summary(data):
    summary = {cat: 0.0 for cat in CATEGORIES}
    for e in data["expenses"]:
        cat = e["category"]
        if cat in summary:
            summary[cat] += e["amount"]
    return summary

def get_total(data):
    return sum(e["amount"] for e in data["expenses"])

def filter_by_category(data, category):
    return [e for e in data["expenses"] if e["category"].lower() == category.lower()]

def filter_by_date(data, date_str):
    return [e for e in data["expenses"] if e["date"].startswith(date_str)]
