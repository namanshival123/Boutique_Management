# This function is used to add new employee details
#     into the employee table in our database by the employer

import mysql.connector

db = mysql.connector.connect(host="localhost",
                             user="root",
                             password='nmnm',
                             database='boutique')

cur = db.cursor()


def add_emp():
    
    h = int(input("enter id: "))
    i = input("enter name: ")
    j = input("enter last name: ")
    k = int(input("enter phone number: "))
    l = input("enter address: ")
    query = "insert into employee values(%s,%s,%s,%s,%s)"
    values = [h, i, j, k, l]
    cur.execute(query, values)
    db.commit()
    print("DETAILS SUCCESSFULLY ADDED")


add_emp()
