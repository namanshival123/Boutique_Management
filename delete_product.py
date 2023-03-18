'''This function is used by the employee of the butique
             to delete product details from the product table.'''

import mysql.connector

db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="nmnm",
                             database="boutique")

cur = db.cursor()


def del_prod():
    import view_product
    g = input("Enter prod_id: ")
    query = ("delete from product where prod_id='{}'".format(g))
    cur.execute(query)
    print("Product deleted sucessfully")
    db.commit()


del_prod()
