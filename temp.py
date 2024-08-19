from enum import Enum

class Account(Enum):
    CREATE  = "1"
    BALANCE = "2"
    UPDATE = "3"
    DEPOSIT = "4"
    WITHDRAW = "1"
    EXIT = ("3","5")

print(Account.EXIT.value[1])

# import mysql.connector # type: ignore
# import uuid


# mydb = mysql.connector.connect(
#   host="127.0.0.1",
#   port=3306,
#   user="root",
#   password="asdf4321",
#   database="mydatabase"
# )
# mycursor = mydb.cursor()

# mycursor.execute(f"select * from temp;")

# myresult = mycursor.fetchall()

# # print(myresult[1][0])

# # for x in myresult:
# #   print(x[1])

# print(uuid.uuid4())

# var = 123.2
# print(type(var))

# # from enum import Enum

# # class Season(Enum):
# #     SPRING = 1
# #     SUMMER = 2
# #     AUTUMN = 3
# #     WINTER = 4
# # print(Season.SPRING)
# # print(Season.SPRING.name)
# # print(Season.SPRING.value)
# # print(type(Season.SPRING))
# # print(repr(Season.SPRING))
# # print(list(Season))

# print(type(str(uuid.uuid4().int)[:8]))