'''this function is used to check weather
a customer with the specific customer id exists or not'''

'''If the customer id exists it will show "you are already a customer"
Else it will show "welcome new customer" '''

import mysql.connector

db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="nmnm",
                             database="boutique")

cur = db.cursor()

id_list = []


def check():
    cur.execute("select * from customer")
    for i in cur:
        id_list.append(i[0])
    print("list of id's of customers:\n", id_list)
    a = int(input("enter your id: "))
    if a in id_list:
        print("YOU ARE ALREADY A CUSTOMER")
    else:
        print("WELCOME NEW CUSTOMER")


check()
