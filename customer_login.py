'''This function allow customer to login their accounts'''

'''First check the customer id entered by the user exist or not
and then give choice to customer to excess the details'''

'''1). View their booked product
   2). Booked a new product
   3). Cancel the booked product'''''

import mysql.connector

db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="nmnm",
                             database="boutique")

cur = db.cursor()
list_id = []


def cust_login():
    cur.execute("select * from customer")
    for i in cur:
        list_id.append(i[0])  # because our first column in our table is customer id column
    c_id = int(input("enter your id: "))
    if c_id in list_id:
        print("Make a choice\n1. view products\n2. update details\n3. cancel booked product")
        choice = int(input("enter your choice 1 or 2 or 3: "))

        if choice == 1:
            import booked_prod
        elif choice == 2:
            new_prod = input("enter new product: ")
            asd = int(input("enter your customer id: "))
            query = ("update customer set booked_prod='{}' where cust_id={}".format(new_prod, asd))
            cur.execute(query)
            print("details updated")

        elif choice == 3:
            asdf = int(input("enter your customer id: "))
            query2 = "delete from customer where cust_id={}".format(asdf)
            cur.execute(query2)
            print("deleted successfully")
        else:
            print("enter valid choice")
    else:
        print("INVALID CUSTOMER ID\nTRY AGAIN...")

    db.commit()


cust_login()
