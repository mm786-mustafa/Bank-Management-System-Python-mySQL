import uuid
from DL.database import db_create_transaction_record, db_withdraw_cash
from DL.database import db_deposit_cash, db_get_customer_record

class Transaction:
    transaction_ID : str = ""
    transaction_details : str = ""
    transaction_amount : float = 0
    account_ID : str = ""
    balance : float = 0

    def deposit_transaction(self):
        print("\n*** Deposit Amount ***")
        print("Enter Customer ID in which the amount will be deposited: ")
        self.user_ID = input("Customer ID: ")
        customer = db_get_customer_record(self.user_ID)
        if customer == None:
            print("Customer not found!")
            return
        self.transaction_amount = float(input("Enter amount you would like to deposit: "))
        self.transaction_ID = str(uuid.uuid4().int)[:8]
        self.account_ID = customer[5]
        self.transaction_details = db_deposit_cash(self.transaction_amount, self.account_ID)
        db_create_transaction_record(self.transaction_ID, self.transaction_details, self.transaction_amount, self.account_ID)
        print("Deposit Transaction Successful!")

    def withdraw_transaction(self,user):
        print("\n*** Withdraw Amount ***")
        self.transaction_amount = float(input("Enter amount you would like to withdraw: "))
        self.balance = user[6]
        self.transaction_ID = str(uuid.uuid4().int)[:8]
        self.account_ID = user[5]
        if self.transaction_amount > self.balance:
            print("Insufficient Balance!")
            self.transaction_details = "Insufficeient Balance"
        else:
            self.transaction_details = db_withdraw_cash(self.transaction_amount,self.account_ID)
            print("Withdraw Transaction Successful!")
        db_create_transaction_record(self.transaction_ID,self.transaction_details,self.transaction_amount,self.account_ID)
