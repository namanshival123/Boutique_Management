#     This function is used to create a new customer account.

'''This function ask customer to enter their customer id and check
if the id exists or not because customer id is a primary key in
customer table in our database and the value entered in it must
be unique.
          If the customer exist it display a message else it takes
the customer details and insert the record in the customer table of the database.'''

import mysql.connector

db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="nmnm",
                             database="boutique")

cur = db.cursor()
# created a list to have all customer id's in it
list_id = []


def new_cust():
    cur.execute("select * from customer")
    for i in cur:
        list_id.append(i[0])  # because our first column in out table is customer id column
    c_id = int(input("enter your id: "))
    if c_id in list_id:
        print("^^YOU ARE ALREADY A CUSTOMER^^^\nCreat a new unique id...")
    else:
        print("WELCOME NEW CUSTOMER\nKINDLY ENTER YOUR DETAILS\n")
        name = input("enter your name: ")
        lname = input("enter your last name: ")
        contact = int(input("enter your contact number: "))
        adrs = input("enter your address: ")
        product = input("enter your booked product: ")

        query = ("insert into customer values(%s,%s,%s,%s,%s,%s)")
        values = [c_id, name, lname, contact, adrs, product]
        cur.execute(query, values)
        print("DETAILS SUCCESSFULLY ADDED")
        db.commit()


new_cust()

