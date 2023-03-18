   # This function allow to login for employee accounts.

'''it allow only to
   1). Add new product to database
   2). Delete a product to database'''

import mysql.connector

db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="nmnm",
                             database="boutique")

cur = db.cursor()
emp_id = []


def emp_login():
    cur.execute('select * from employee')
    for i in cur:
        emp_id.append(i[0])
    print(emp_id)
    a = int(input("Enter your employee id:"))
    if a in emp_id:
        print("1). Add new product\n2). delete product")
        b = int(input("Enter here:.. "))
        if b == 1:
            import add_product
        elif b == 2:
            import delete_product
        else:
            print("INVALID CHOICE")
    else:
        print("INVALID EMPLOYEE ID")


emp_login()
