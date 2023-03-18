# This function is for employer login and allow the
#         employer to view all products and add new employees.

import mysql.connector

db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="nmnm",
                             database="boutique")

cur = db.cursor()


def employer_login():
    print("1. To view all product\n2. To add a new employee")
    choice3 = int(input("ENTER YOUR CHOICE: "))
    if choice3 == 1:
        import view_product
    elif choice3 == 2:
        import add_emp
    else:
        print("invalid choice")


employer_login()
