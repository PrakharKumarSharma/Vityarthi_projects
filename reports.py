from expenses import expenses

def total_expense():
    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal Expense: ₹{total}")

def category_wise_totals():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nCategory-wise Summary")
    summary = {}

    for e in expenses:
        cat = e["category"]
        amt = e["amount"]
        if cat not in summary:
            summary[cat] = 0
        summary[cat] += amt

    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")

def highest_expense():
    if not expenses:
        print("No expenses recorded.")
        return

    max_exp = max(expenses, key=lambda e: e["amount"])
    print("\nHighest Expense:")
    print(f"₹{max_exp['amount']} - {max_exp['category']} - {max_exp['note']}")

def report_menu():
    while True:
        print("\nReports Menu")
        print("1. Total Expense")
        print("2. Category-wise Report")
        print("3. Highest Expense")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1": total_expense()
        elif choice == "2": category_wise_totals()
        elif choice == "3": highest_expense()
        elif choice == "4": break
        else: print("Invalid choice")
