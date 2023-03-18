'''This function fatches all product details
        from database and display them in the form of a table.'''

import mysql.connector

db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="nmnm",
                             database="boutique")
cur = db.cursor()


def view_prod():
    query = 'select * from product'
    cur.execute(query)
    print("pr_no   p_id   price   stock")
    for i in cur:
        print(i)


view_prod()
