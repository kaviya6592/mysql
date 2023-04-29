from datetime import date

import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Thanku@123",
  database="shop"
)
# assignment:
# 1)write a python program with SQL queries to find the errors in the database; one of the item_id's in 'item' is used twice and there has been a sale of a product which does not exist.


# 2)You can also use a scary SQL query to find the double items; SELECT t1.item_id from items t1 INNER JOIN items t2 WHERE t1.id > t2.id AND t1.item_id = t2.item_id;

# 3)Can you think of a single query to find the item_id in the sales table of the non-existent product?


# 4)Write a program that orders the sales on date and prints the date, the description and the amounts.


# 5)Write a program to find the best selling product and print that.

mycursor = mydb.cursor()

# sql="CREATE TABLE items1 ( id INT unsigned NOT NULL AUTO_INCREMENT, item_id INT NOT NULL, description varchar(255) NOT NULL, PRIMARY KEY (id) ) "
# mycursor.execute(sql)

# sql="INSERT INTO items1 (item_id, description) VALUES (%s, %s)"
# val= [('1002', 'apple'),
#    ('1003', 'computer'),
#    ('1004', 'mango'),
#    ('1005', 'book'),
#    ('1006', 'airplane'),
#    ('1007', 'car'),
#    ('1007', 'melon'),
#    ('1008', 'bread'),
#    ('1009', 'tomato'),
#    ('1010', 'phone'),
#    ('1011', 'dog'),
#    ('1012', 'cat'),
#    ('1013', 'fish'),
#    ('1014', 'flower')
#  ]
#
# mycursor.executemany(sql, val)
#
#

# mycursor.execute("SELECT item_id ,COUNT(item_id) FROM items1 GROUP BY item_id HAVING COUNT(item_id)>1")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#
#   print(x)

#
# mydb.commit()

# sql="CREATE TABLE sales1( id INT unsigned NOT NULL AUTO_INCREMENT,date date NOT NULL ,item_id INT NOT NULL, amount INT NOT NULL, PRIMARY KEY (id) ) "
# mycursor.execute(sql)
# sql="INSERT INTO sales1 (date, item_id, amount) VALUES(%s,%s,%s)"
# val=[
#   ("2022-10-10", 1005, 3),
#  ("2022-10-11", 1003, 30),
#  ("2022-9-11", 1001, 3),
#  ("2022-9-11", 1011, 3),
#  ( "2022-10-12", 1002, 5),
#   ("2022-10-12", 1004, 15),
#   ("2022-10-12", 1008, 1),
#   ("2022-10-12", 1007, 3),
#   ("2022-10-14", 1007, 12),
#   ("2022-10-15", 1012, 1),
#   ("2022-10-15", 1009, 6),
#   ("2022-10-15", 1008, 4),
#   ("2022-10-16", 1009, 4),
#  ("2022-10-16", 1011, 5),
#  ("2022-10-16", 1014, 50),
#   ("2022-10-17", 1016, 50),
#   ("2022-10-18", 1002, 7),
#   ("2022-10-19", 1003, 3),
#   ("2022-10-19", 1002, 8)
# ]
# #      ]
# #
# mycursor.executemany(sql,val)
# #
# #
# #
# #
# print(mycursor.rowcount, "record was inserted.")
# #
# #
# #
# #



#inner join query

# sql="SELECT items1.item_id item_id, sales.item_id FROM items1 INNER JOIN t2 WHERE t1.id > t2.id AND t1.item_id = t2.item_id;"
# try:
#   cnx = mysql.connector.connect(user='scott', database='employees')
#   cursor = cnx.cursor()
#   cursor.execute("SELECT * FORM employees")   # Syntax error in query
#   cnx.close()
# except mysql.connector.Error as err:
#   print("Something went wrong: {}".format(err))

#
# sql="SELECT description FROM items1 WHERE item_id=item_id"
# sql="SELECT description FROM items1 WHERE EXISTS (SELECT description FROM items1 WHERE items1.item_id= items1.item_id"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print("hallo")
#
#   print(x)
print("Find duplicate in item table")
mycursor.execute("SELECT item_id ,COUNT(item_id) FROM items1 GROUP BY item_id HAVING COUNT(item_id)>1")
myresult = mycursor.fetchall()

for x in myresult:
  if x[1]>1:
    print(f"table has duplicate values. table has item_id {x[0]} is repeated {x[1]} times")
    print(x)
    break
  else:
    print("table has no duplicate values")

print("sales table oreder by date")
sql="SELECT * FROM sales ORDER BY date"
mycursor.execute(sql)
myresult_1= mycursor.fetchall()
print(myresult_1)

print("display whole item table")
sql = "SELECT * FROM items1"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
  print(x)


print("find double item in item table")
sql1="SELECT t1.item_id from items1 t1 INNER JOIN ITEMS1 t2 WHERE t1.id>t2.id AND t1.item_id=t2.item_id"
mycursor.execute(sql1)
myresult1=mycursor.fetchall()
print("items table")
for x in myresult1:
  print(x)

#find double item_id in sales table
#sql2="SELECT s1.item_id from sales1 s1 INNER JOIN sales1 s2 WHERE s1.id>s2.id AND s1.item_id=s2.item_id"
sql2="SELECT item_id ,COUNT(item_id) FROM sales1 GROUP BY item_id HAVING COUNT(item_id)>1"
mycursor.execute(sql2)
myresult2=mycursor.fetchall()
print("sales table")
for x in myresult2:
  print(x)


print("display date description amount")
# sql3="SELECT sales.date,sales.amount,items1.description FROM sales1 JOIN items1 WHERE "
sql4="SELECT s.date,t.description,s.amount FROM sales1 s,items1 t WHERE t.item_id=s.item_id"
mycursor.execute(sql4)
myresult4=mycursor.fetchall()
print("join sales and item  table")
for x in myresult4:
  print(x)

print("best selling product")
sql5="SELECT item_id,COUNT(item_id) FROM sales1 GROUP BY item_id HAVING COUNT(item_id)>1"
mycursor.execute(sql5)
myresult5=mycursor.fetchall()

for x in myresult5:
  if x[1]>2:
    sql6="SELECT description FROM items1 WHERE item_id=%s"
    val=[x[0]]
    mycursor.execute(sql6,val)
    myresult6 = mycursor.fetchall()

    print(f"Best selling product id {x[0]} product name {myresult6[0]}")







