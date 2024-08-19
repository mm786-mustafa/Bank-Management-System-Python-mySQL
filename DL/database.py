import mysql.connector # type: ignore

mydb = mysql.connector.connect(
  host="127.0.0.1",
  port=3306,
  user="root",
  password="asdf4321",
  database="bms"
)
mycursor = mydb.cursor()

# *** Create Record ***
def db_create_account_record(account_id,balance,user_id):
    mycursor.execute(f"INSERT INTO accounts VALUES (\"{account_id}\",{balance},\"{user_id}\")")
    mydb.commit()

def db_create_user_record(user_id,name,username,password,account_type):
    mycursor.execute(f"INSERT INTO users VALUES (\"{user_id}\",\"{name}\",\"{username}\",\"{password}\",\"{account_type}\")")
    mydb.commit()

def db_create_transaction_record(transaction_id,transaction_details,transaction_amount,account_id):
    mycursor.execute(f"INSERT INTO transactions VALUES (\"{transaction_id}\",\"{transaction_details}\",{transaction_amount},\"{account_id}\")")
    mydb.commit()

# *** Update Record ***
def db_update_name(new_name,user_id): 
    mycursor.execute(f"Update users SET name=\"{new_name}\" WHERE userID=\"{user_id}\"")
    mydb.commit()
    

def db_update_username(new_username,user_id):
    mycursor.execute(f"Update users SET username=\"{new_username}\" WHERE userID=\"{user_id}\"")
    mydb.commit()

def db_update_password(new_password,user_id):
    mycursor.execute(f"Update users SET password=\"{new_password}\" WHERE userID=\"{user_id}\"")
    mydb.commit()

# *** Get Record *** 
def db_get_user_record(username):
    mycursor.execute(f"SELECT * FROM users LEFT OUTER JOIN accounts ON users.userID=accounts.userID WHERE users.username=\"{username}\";")
    user = mycursor.fetchone()
    return user

def db_get_customer_record(user_id):
    mycursor.execute(f"SELECT * FROM users INNER JOIN accounts ON users.userID=accounts.userID WHERE users.userID=\"{user_id}\";")
    user = mycursor.fetchone()
    return user

def db_get_user_account_balance(user_id):
    mycursor.execute(f"SELECT balance FROM accounts WHERE userID=\"{user_id}\";")
    current_balance = mycursor.fetchone()
    return current_balance[0]

def db_get_transaction_record(account_id):
    mycursor.execute(f"select transactions.transactionID, transactions.transactionDetails, transactions.amount from transactions INNER JOIN accounts ON transactions.accountID=accounts.accountID WHERE accounts.accountID=\"{account_id}\";")
    records = mycursor.fetchall()
    return records

# *** Transactional Records / Updating Record Related to Balance ***
def db_deposit_cash(deposit_amount,account_id):
    mycursor.execute(f"UPDATE accounts SET balance=balance+{deposit_amount} WHERE accountID=\"{account_id}\"")
    mydb.commit()
    return "Deposit  Successful!"
    

def db_withdraw_cash(withdraw_amount,account_id):
    mycursor.execute(f"UPDATE accounts SET balance=balance-{withdraw_amount} WHERE accountID=\"{account_id}\"")
    mydb.commit()
    return "Withdraw Successful!"