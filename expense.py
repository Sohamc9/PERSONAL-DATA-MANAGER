import pandas as pd
from storage import load_data , save_data

FILE = "data/expenses.csv"
COLUMNS = ["Date", "Amount", "Category","Note"]

from datetime import date

def add_expense(amount, category, note):
    if amount <= 0:
        print("Amount must be greater than 0.")

        return
    
    df = load_data(FILE, COLUMNS)

    new_row = {"Date": date.today(),
               "Amount": amount,
               "Category": category,
               "Note": note}
    
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_data(df, FILE)
    print("Expense added successfully.")


def view_expenses():
    df = load_data(FILE, COLUMNS)
    if df.empty:
        print("No expenses found.")
    else:
        print(df.to_string(index=False))
        input("\n Press Enter to continue...")

def delete_expense(index):
    df = load_data(FILE, COLUMNS)
    if 0<= index < len(df):
        df = df.drop(index).reset_index(drop=True)
        save_data(df, FILE)
        print("Expense deleted")
    else:
        print("Invalid index.")


def expense_summary():
    df = load_data(FILE, COLUMNS)
    if df.empty:
        print("No expenses found")
        return
    
    total = df["Amount"].sum()
    print(f"\n==== Expense Summary ====")
    print(f"Total Expenses: ₹{total}") 
    print("\nExpenses by Category:")
    print(df.groupby("Category")["Amount"].sum()).to_string()
    input("\n Press Enter to continue...") 