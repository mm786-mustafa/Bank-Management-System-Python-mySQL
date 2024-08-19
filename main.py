from BL import bankAccount
from BL import customer
from BL import transaction
from DL.database import db_get_user_record
from enum import Enum

class Users(Enum):
    ADMIN = "admin"
    CUSTOMER = "user"

class Account(Enum):
    CREATE  = "1"
    BALANCE = "2"
    UPDATE = "3"
    DEPOSIT = "4"
    RECORDS = "5"
    WITHDRAW = "1"
    EXIT = ("3","6")

def main():
    print("*** Welcome to Bank Management System ***")
    print("\nEnter the following credentials to login: ")
    
    username = input("Username: ")
    password = input("Password: ")
    user = db_get_user_record(username)

    if user == None:
        print("\nUser not found!")
        exit()
    
    while True:    
        if password == user[3]:
            print("Access Granted!")
            if user[4] == Users.ADMIN.value:
                admin_view()
            else:
                customer_view(user)
        else:
            print("\nInvalid Password!")
            password = input("Enter Password Again: ")


def admin_view():
    while True:
        print("\nWhat would you like to do: ")
        print("1. Create New Account")
        print("2. Check Account Balance")
        print("3. Update Account")
        print("4. Deposit Balance")
        print("5. Transaction Records")
        print("6. Logout")
        selection = input("Enter your choice: ")

        if selection == Account.EXIT.value[1]:
            print("Logged Out!")
            exit()
        elif selection == Account.CREATE.value:
            bankAccount.BankAccount().create_user_account()
        elif selection == Account.BALANCE.value:
            bankAccount.BankAccount().check_account_balance()
        elif selection == Account.UPDATE.value:
            bankAccount.BankAccount().update_account()
        elif selection == Account.DEPOSIT.value:
            transaction.Transaction().deposit_transaction()
        elif selection == Account.RECORDS.value:
            bankAccount.BankAccount().view_customer_transactions()
        else:
            print("Invalid Choice!")

def customer_view(user):
    while True:
        print("\nWhat would you like to do: ")
        print("1. Withdraw Balance")
        print("2. Check Account Balance")
        print("3. Logout")
        selection = input("Enter your choice: ")
        
        if selection == Account.EXIT.value[0]:
            print("Logged Out!")
            exit()
        elif selection == "1":
            transaction.Transaction().withdraw_transaction(user)
        elif selection == "2":
            customer.Customer().check_account_balance(user)
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()