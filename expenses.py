from models import Expense

expenses = []
def add(amount, description):
    expense = Expense(amount, description)
    expenses.append(expense)
    
def show_list():
    if not expenses:
        print("No expenses")
    else:
        print("Amount", "=============", "Description")
        for expense in expenses:
            print(expense.amount, "=============", expense.description)


def update_expense(index, amount, description):
    if 0 <= index < len(expenses):
        expenses[index].amount = amount
        expenses[index].description = description
        print("Expense updated successfully")
        print("Updated expense id:", expenses[index])
        print("Updated expense amount:", expenses[index].amount)
        print("Updated expense description:", expenses[index].description)
        
    else:
        print("Invalid expense index.")
        
def delete_expense():
    if not expenses:
        print("No expenses to delete")
        return
    for i, expense in enumerate(expenses):
        print(f"{i + 1} : {expense.amount} - {expense.description}")
    choice = input("Enter the number of the expense you want to delete:")
    
    try:
        choice = int(choice)
        if 1<= choice <= len(expenses):
            del expenses[choice - 1]
            print("Expense deleted successfully")
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid choice")
        
def generate_report():
    total = sum(expense.amount for expense in expenses)
    return f"Total expenses : {total}"