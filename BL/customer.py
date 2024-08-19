from DL.database import db_get_user_account_balance

class Customer:
    withdraw_amount : float = 0
    balance : float = 0
    account_ID : str = ""

    def check_account_balance(self,user):
        print("\n*** Checking Account Balance ***")
        self.balance = db_get_user_account_balance(user[0])
        print(f"Your Current Balance: {self.balance}")