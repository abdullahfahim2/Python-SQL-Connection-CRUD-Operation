import mysql.connector

host = input("Enter Your Database Host Name: ")
user = input("Enter Your Database Username: ")
passwd = input("Enter Your Database Username: ")

con = mysql.connector.connect(host = host , user = user , passwd = passwd)

#Checking Database Connection
def check():  
    print(con)
    if con:
        print("Connection Succesfull")
    else:
        print("Connection Unsuccesfull")

#creating Cursor in Database
mycursor = con.cursor()

#Creating Database
def createdb():
    mycursor.execute("create database CompanyList;")
    print("Database Created!")

#Show Databases
def showdb():
    mycursor.execute("Show Databases;")
    print("All Databases in Your Host :")
    for i in mycursor:
        print(i)

#adding database to con
datab = input("Enter Database Name: ")
con = mysql.connector.connect(host = host , user = user , passwd = passwd , database = datab)
mycursor = con.cursor()

#create table in your Database
def create_table():
    mycursor.execute("create table employee(no INT , Name VARCHAR(55) , Designation VARCHAR(55) , Salary INT);")
    print("Table Created In Your Selected Database!")

#Insert Data in Table
def insert_data():
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
    print("Data Inserted To Your Selected Database Table!")

#read data from database table
def read_data():
    mycursor.execute("select * from employee;")
    result = mycursor.fetchall()

    print("Data in Your Table : ")

    for i in result:
        print(i)

#update data in table
def update_data():
    mycursor.execute("update employee set Salary = 15000 where no = 101;")
    con.commit()
    print("Your Data Updated!")

#Delete Data in Table
def delete_data():
    mycursor.execute("delete from employee where no = 105;")
    con.commit()
    print("Your Selected Data Is Deleted!")

#Search from table
def search_data():
    mycursor.execute("select * from employee where no =104;")
    s = mycursor.fetchone()
    print(s)



print("Select Your Preferd Operations:\n1.Check Your Database Connection\n2.Create Database\n3.Show Database")
print("4.Create Table\n5.Insert Data in Table\n6.Read Data\n7.Update Data\n8.Delete Data\n9.Search Data\n10.Exit")

while True:

    ch = int(input("Enter Your Choice: \n"))

    if ch == 1:
        check()
    elif ch == 2:
        createdb()
    elif ch == 3:
        showdb()
    elif ch == 4:
        create_table()
    elif ch == 5:
        insert_data()
    elif ch == 6:
        read_data()
    elif ch == 7:
        update_data()
    elif ch == 8:
        delete_data()
    elif ch == 9:
        search_data()
    elif ch == 10:
        print("Thanks For Using This System!\nFeel Free To Ask Me Anything!")
        print("Contact Me : aafahim4320@gmail.com")
        break
        
    else:
        print("You Entered an Invalid Choice!")
