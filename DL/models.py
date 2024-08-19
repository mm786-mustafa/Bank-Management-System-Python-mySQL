# create table users(
# 	userID varchar(255) Primary Key,
#     name varchar(255) not null,
#     username varchar(255) not null,
#     password varchar(255) not null,
#     type varchar(255)
# );

# create table accounts(
# 	accountID varchar(255) Primary Key,
#     balance float,
#     userID varchar(255),
#     Foreign key (userID) references users(userID)
# );

# create table transactions(
# 	transactionID varchar(255) Primary Key,
#     transactionDetails varchar(255),
#     amount float,
#     accountID varchar(255),
#     Foreign Key (accountID) references accounts(accountID)
# );
