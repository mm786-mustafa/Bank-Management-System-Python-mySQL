import uuid
from DL.database import db_create_account_record, db_create_user_record, db_update_password, db_update_name
from DL.database import db_get_customer_record, db_update_username, db_get_transaction_record
from enum import Enum

def validate_name(name):
    valid_name = name
    is_valid = False
    while not is_valid:
        if all(c.isalpha() or c.isspace() for c in valid_name):
            is_valid = True
        else:
            print("\nInvalid Name! Enter only alphabets.")
            valid_name = input("Enter Name Again: ")
    return valid_name

class Update(Enum):
    NAME = 1
    USERNAME = 2
    PASSWORD = 3

class BankAccount:
    user_ID : str = ""
    account_ID : str = ""
    name : str = ""
    username : str = ""
    password : str = ""
    account_type : str = ""
    balance : float = 0

    def create_user_account(self):
        print("\n*** Creating Account ***")
        print("\nEnter account holder credentials: ")
        self.user_ID = str(uuid.uuid4().int)[:8]
        self.name = input("Name: ")
        self.name = validate_name(self.name)
        self.username = input("Username: ")
        self.username = validate_name(self.username)
        self.password = input("Password: ")
        self.account_type = "user"
        self.account_ID = str(uuid.uuid4().int)[:8]
        self.balance = float(input("Enter initial balance: "))
        db_create_user_record(self.user_ID,self.name,self.username,self.password,self.account_type)
        db_create_account_record(self.account_ID,self.balance,self.user_ID)
        print("Account Created Successfully!")

    def update_account(self):
        print("\n*** Updating Account ***")
        print("Enter Customer ID you want to update: ")
        self.user_ID = input("Customer ID: ")
        customer = db_get_customer_record(self.user_ID)
        if customer == None:
            print("Customer not found!")
            return
        print("\nWhat would you like to update:\n1. Name\n2. Username\n3. Password")
        selection = int(input("Enter your choice: "))

        if selection == Update.NAME.value:
            new_name = input("Enter New Name: ")
            db_update_name(new_name,customer[0])
            print("Name Updated Successfully!")
        elif selection == Update.USERNAME.value:
            new_username = input("Enter New Username: ")
            db_update_username(new_username,customer[0])
            print("Username Updated Successfully!")
        elif selection == Update.PASSWORD.value:
            new_password = input("Enter New Password: ")
            db_update_password(new_password,customer[0])
            print("Password Updated Successfully!")
        else:
            print("Invalid Choice!")

    def check_account_balance(self):
        print("\n*** Checking Account Balance ***")
        print("Enter Customer ID whose account balance you want to review: ")
        self.user_ID = input("Customer ID: ")
        customer = db_get_customer_record(self.user_ID)
        if customer == None:
            print("Customer not found!")
            return
        self.balance = customer[6]
        print(f"\nCustomer's Current Balance: {self.balance}")

    def view_customer_transactions(self):
        print("\n*** Checking Account Balance ***")
        print("Enter Customer ID whose account balance you want to review: ")
        self.user_ID = input("Customer ID: ")
        customer = db_get_customer_record(self.user_ID)
        if customer == None:
            print("Customer not found!")
            return
        transaction_records = db_get_transaction_record(customer[5])
        if transaction_records == None:
            print("No record found!")
            return
        print("\n*** Transactions Records ***")
        print(f"Name: {customer[1]} \nAccount ID: {customer[5]} \nCurrent Balance: {customer[6]}")
        print("\nTransaction-ID   Transaction-Status     Transaction-Amount")
        for record in transaction_records:
            print(f"* {record[0]}       {record[1]}   {record[2]}") 