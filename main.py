#CRUD Operation With Python & SQL
#edit the Comments for the Operation

import mysql.connector

con = mysql.connector.connect(host = "localhost" , user = "testuser" , passwd = "test12345" , database = "CompanyList")


"""#Checking Database Connection
print(con)
if con:
    print("Connection Succesfull")

else:
    print("Connection Unsuccesfull")"""

#creating Cursor in Database
mycursor = con.cursor()

"""#Creating Database
mycursor.execute("create database CompanyList;")
print("Database Created!")"""

"""#Show Databases
mycursor.execute("Show Databases;")

print("All Databases in Your Host :")

for i in mycursor:
    print(i)"""

"""#create table in your Database
#Firstly Connect your database with con Variable by adding database attribute and your database as value!

mycursor.execute("create table employee(no INT , Name VARCHAR(55) , Designation VARCHAR(55) , Salary INT);")
print("Table Created In Your Selected Database!")"""

"""#Insert Data in Table
#Single Data Entry
#mycursor.execute("insert into employee(no , Name , Designation , Salary) values (101 , 'karim' , 'manager' , 20000)")

#multiple Data Entry
insertdata = ("insert into employee(no , Name , Designation , Salary) values (%s , %s , %s , %s)")
value = [
    (102 , 'Shamim' , 'Marketing Head' , 18000),
    (103 , 'Tanbir' , 'Graphics Designer' , 18000),
    (104 , 'Jilane' , 'Network administrator' , 18000),
    (104 , 'Hasan' , 'Clerk' , 12000)
]

mycursor.executemany(insertdata , value)

con.commit()
print("Data Inserted To Your Selected Database Table!")"""

"""#read data from database table
mycursor.execute("select * from employee;")
result = mycursor.fetchall()

print("Data in Your Table : ")

for i in result:
    print(i)"""

"""#update data in table

mycursor.execute("update employee set Salary = 15000 where no = 101;")
con.commit()
print("Your Data Updated!")"""

"""#Delete Data in Table

mycursor.execute("delete from employee where no = 105;")
con.commit()
print("Your Selected Data Is Deleted!")"""

"""#Search from table

mycursor.execute("select * from employee where no =104;")
s = mycursor.fetchone()
print(s)"""
