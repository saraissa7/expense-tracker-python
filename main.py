import pandas as pd
from datetime import datetime
import os

FILE_NAME = "expenses.csv"

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    date = datetime.now().strftime("%Y-%m-%d")

    data = [[name, amount, date]]
    df = pd.DataFrame(data, columns=["Name", "Amount", "Date"])

    if os.path.exists(FILE_NAME):
        df.to_csv(FILE_NAME, mode="a", header=False, index=False)
    else:
        df.to_csv(FILE_NAME, index=False)

    print("Expense saved.")

def generate_report():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    df = pd.read_csv(FILE_NAME)
    summary = df.groupby("Name")["Amount"].sum()

    print("\nExpense Summary:")
    print(summary)

    summary.to_excel("expense_report.xlsx")

    print("\nExcel report created: expense_report.xlsx")

def main():
    while True:
        print("\n1. Add expense")
        print("2. Generate report")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            generate_report()

        elif choice == "3":
            break

        else:
            print("Invalid choice")

main()