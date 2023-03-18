'''This function is used by the employee of the boutique to add new product'''

'''It asks for the details of the product and enter
        the new record into the product table in database.'''

import mysql.connector

db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="nmnm",
                             database="boutique")

cur = db.cursor()


def add_prod():
    p_no = int(input("enter product number: "))
    p_id = input("enter product id: ")
    p_price = int(input("enter product price: "))
    p_stock = int(input("enter product stock: "))
    query3 = "insert into product values(%s,%s,%s,%s)"
    values = [p_no, p_id, p_price, p_stock]
    cur.execute(query3, values)
    print("Product added successfully")
    db.commit()


add_prod()
