# Bank-Management-System
 
In this project, I have created Bank Management System using Python and mySQL. It includes three entites: BankAccount,Customer and Transactions each of which are stored in BL(Bussiness Layer). Whereas as database.py where queries exist is located in DL(DataAccess Layer).

There are two types of users: Admin and Customers

Admin has rights to:
1. Create Customer
2. Update Customer
3. Deposit Cash to Customer Account
4. Check account balance of Customer
5. Check Transaction History of Customer

Whereas Customer has rights to:
1. Withdraw cash from account
2. Check account balance

For creating and maintaining project environment, I have used "poetry".

Following dependencies were installed:
1. uuid (To generate customer id and account id)
2. mysql-connector-python (For connecting local established mySQL database.)
