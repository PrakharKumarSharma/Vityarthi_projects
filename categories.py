categories = ["Food", "Travel", "Shopping", "Bills"]

def view_categories():
    print("\nCategories:")
    for i, c in enumerate(categories):
        print(f"{i+1}. {c}")

def add_category():
    new_cat = input("Enter new category: ")
    if new_cat in categories:
        print("Category already exists!")
    else:
        categories.append(new_cat)
        print("Category added!")

def delete_category():
    view_categories()
    try:
        num = int(input("Enter category number to delete: "))
        categories.pop(num-1)
        print("Category removed")
    except:
        print("Invalid input")

def category_menu():
    while True:
        print("\nCategory Menu")
        print("1. View Categories")
        print("2. Add Category")
        print("3. Delete Category")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1": view_categories()
        elif choice == "2": add_category()
        elif choice == "3": delete_category()
        elif choice == "4": break
        else: print("Invalid choice")
