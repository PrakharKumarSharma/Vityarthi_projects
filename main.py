from expenses import *
from reports import *
from categories import *

def main_menu():
    while True:
        print("EXPENSE TRACKER ")
        print("1. Expense Management")
        print("2. Category Management")
        print("3. Reports")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            expense_menu()
        elif choice == "2":
            category_menu()
        elif choice == "3":
            report_menu()
        elif choice == "4":
            print("Exiting program")
            break
        else:
            print("Invalid choice! Try again.")

main_menu()
