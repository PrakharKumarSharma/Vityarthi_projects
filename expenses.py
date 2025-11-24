expenses = []  
# each expense → {"amount": 200, "category": "Food", "note": "Lunch"}

def add_expense():
    try:
        amount = float(input("Enter amount: "))
    except:
        print("Invalid amount")
        return

    category = input("Enter category: ")
    note = input("Enter note/description: ")

    expenses.append({
        "amount": amount,
        "category": category,
        "note": note
    })

    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- All Expenses ---")
    for i, e in enumerate(expenses):
        print(f"{i+1}. ₹{e['amount']} - {e['category']} - {e['note']}")

def delete_expense():
    view_expenses()
    if not expenses:
        return

    try:
        num = int(input("Enter expense number to delete: "))
        expenses.pop(num-1)
        print("Expense removed!")
    except:
        print("Invalid selection!")

def expense_menu():
    while True:
        print("\nExpense Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1": add_expense()
        elif choice == "2": view_expenses()
        elif choice == "3": delete_expense()
        elif choice == "4": break
        else: print("Invalid choice!")
