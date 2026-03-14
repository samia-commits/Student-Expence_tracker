from colorama import init, Fore, Style
from tabulate import tabulate
from storage import load_data, save_data
from expenses import (
    add_expense, delete_expense, get_summary,
    get_total, filter_by_category, filter_by_date, CATEGORIES
)

init(autoreset=True)

def print_menu():
    print(Fore.CYAN + "\n=== Student Expense Tracker ===")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Delete expense")
    print("4. View summary by category")
    print("5. Filter by category")
    print("6. Filter by date")
    print("7. Set budget")
    print("8. View total & budget status")
    print("0. Exit")

def main():
    data = load_data()

    while True:
        print_menu()
        choice = input(Fore.YELLOW + "\nChoice: ").strip()

        if choice == "1":
            try:
                amount = float(input("Amount: "))
            except ValueError:
                print(Fore.RED + "Invalid amount.")
                continue
            print("Categories:", ", ".join(CATEGORIES))
            category = input("Category: ").strip().capitalize()
            if category not in CATEGORIES:
                print(Fore.RED + "Invalid category.")
                continue
            desc = input("Description: ").strip()
            expense = add_expense(data, amount, category, desc)
            save_data(data)
            print(Fore.GREEN + f"Added: #{expense['id']} {expense['category']} ${expense['amount']:.2f}")

        elif choice == "2":
            if not data["expenses"]:
                print("No expenses yet.")
            else:
                print(tabulate(data["expenses"], headers="keys", tablefmt="rounded_outline"))

        elif choice == "3":
            try:
                eid = int(input("Expense ID to delete: "))
            except ValueError:
                print(Fore.RED + "Invalid ID.")
                continue
            if delete_expense(data, eid):
                save_data(data)
                print(Fore.GREEN + "Deleted.")
            else:
                print(Fore.RED + "ID not found.")

        elif choice == "4":
            summary = get_summary(data)
            rows = [[cat, f"${amt:.2f}"] for cat, amt in summary.items() if amt > 0]
            print(tabulate(rows, headers=["Category", "Total"], tablefmt="rounded_outline") if rows else "No expenses.")

        elif choice == "5":
            cat = input("Category: ").strip().capitalize()
            results = filter_by_category(data, cat)
            print(tabulate(results, headers="keys", tablefmt="rounded_outline") if results else "No results.")

        elif choice == "6":
            date = input("Date (YYYY-MM-DD): ").strip()
            results = filter_by_date(data, date)
            print(tabulate(results, headers="keys", tablefmt="rounded_outline") if results else "No results.")

        elif choice == "7":
            try:
                data["budget"] = float(input("Set budget: $"))
                save_data(data)
                print(Fore.GREEN + f"Budget set to ${data['budget']:.2f}")
            except ValueError:
                print(Fore.RED + "Invalid amount.")

        elif choice == "8":
            total = get_total(data)
            budget = data.get("budget", 0.0)
            print(f"\nTotal spent: ${total:.2f}")
            if budget > 0:
                remaining = budget - total
                color = Fore.GREEN if remaining >= 0 else Fore.RED
                print(f"Budget: ${budget:.2f}")
                print(color + f"Remaining: ${remaining:.2f}")

        elif choice == "0":
            print("Bye!")
            break
        else:
            print(Fore.RED + "Invalid option.")

if __name__ == "__main__":
    main()
