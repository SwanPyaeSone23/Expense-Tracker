from expenses import add, show_list, generate_report, delete_expense, update_expense

def main():
    while True:
        print("1 : Add Expense")
        print("2 : List Expense")
        print("3 : Update Report")
        print("4 : Delete Expense")
        print("5 : Generate Total Expense Report")
        print("6 : Exit")
        
        choice = input("Enter your choice:")
        
        if choice == "1":
            amount = float(input("Enter the amount:"))
            if amount < 0 or amount == "":
                print("Invalid amount")
                break
            else:
                description = input("Enter the description:")
                if description == "":
                    print("Invalid description")
                    break
                else:
                    add(amount, description)
        elif choice == "2":
            show_list()
        elif choice == "3":
            id = int(input("Enter the id to update : "))
            if id == "":
                print("Invalid id")
                break
            else:
                amount = float(input("Enter the amount:"))
                if amount < 0 or amount == "":
                    print("Amount is invalid")
                    break
                else:
                    description = input("Enter the description:")
                    if description == "":
                        print("Description is invalid")
                        break
                    else:
                        update_expense(id - 1, amount, description)
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            report = generate_report()
            print(report)
        elif choice == "6":
            print("Goodbye")            
            break
            
            
            
if __name__ == "__main__":
    main()