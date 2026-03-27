import pandas as pd
from storage import load_data , save_data
from datetime import date

FILE = "data/tasks.csv"
COLUMNS = ["Title","Deadline", "Priority", "Status", "Note"]
   

def add_task(title, priority, note):
    if title.strip() == "":
        print("Title cannot be empty")
        return
    
    if priority not in ["Low", "Medium", "High"]:
        print("Priority must be Low, Medium, or High")
        return
    
    df = load_data(FILE, COLUMNS)

    new_row = {"Title": title,
               "Deadline": date.today(),    
               "Priority": priority,
               "Status": "Pending",
               "Note": note}

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_data(df, FILE)
    print("Task added successfully.")


def view_tasks():
    df = load_data(FILE, COLUMNS)
    if df.empty:
        print("No tasks found.")
    else:
        print(df.to_string(index=False))
        input("\n Press Enter to continue...")


def delete_task(index):
    df = load_data(FILE, COLUMNS)
    if 0<= index < len(df):
        df = df.drop(index).reset_index(drop=True)
        save_data(df, FILE)
        print("Task deleted")
    else:
        print("Invalid index.")