from expense import add_expense, view_expenses, delete_expense
from utils import get_float, get_int
from task import add_task, view_tasks, delete_task

def menu():
    while True:
        print("\n==== Personal Data Manager ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        print("5. Add Task")
        print("6. View Tasks")
        print("7. Delete Task")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = get_float("Amount: ")
            category = input("Category:")
            note = input("Note:")
            add_expense(amount, category, note)
        
        elif choice == "2":
            view_expenses()

        elif choice == "3":
            index = get_int("Enter index to delete: ")
            delete_expense(index)

        elif choice == "4":
            print("Goodbye...")
            break

        elif choice == "5":
            title = input("Title: ")
            priority = input("Priority (Low, Medium, High): ")
            note = input("Note:")
            add_task(title, priority, note)

        elif choice == "6":
            view_tasks()

        elif choice == "7":
            index = get_int("Enter index to delete: ")
            delete_task(index)

        else:
            print("Invalid choice. Try again.")

menu()