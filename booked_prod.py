'''This function returns a list of products booked by a customer
using the customer id.'''

import mysql.connector

db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="nmnm",
                             database="boutique")

cur = db.cursor()


def booked_prod():
    print("PLEASE ENTER YOUR VALID CUSTOMER ID")
    cust_idd = int(input("ENTER YOUR CUSTOMER ID: "))
    query = 'select booked_prod from customer where cust_id={}'.format(cust_idd)
    cur.execute(query)
    print("YOUR BOOKED PRODUCT\n")
    for i in cur:
        print(i)


booked_prod()
