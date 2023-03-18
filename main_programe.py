import mysql.connector

db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="nmnm",
                             database="boutique")

cur = db.cursor()


def main():
    print("HELLO USER\nENTER 1 TO LOGIN AS CUSTOMER\nENTER 2 TO LOGIN AS EMPLOYEE\nENTER 3 TO LOGIN AS EMPLOYER")
    ch = int(input("ENTER YOUR CHOICE HERE: "))
    if ch == 1:
        ch1 = int(input("ENTER 1 TO CREATE A NEW ACCOUNT\nENTER 2 TO LOGIN INTO EXISTING ACCOUNT"))
        if ch1 == 1:
            import new_cust
        elif ch1 == 2:
            import customer_login
        else:
            print("INVALID CHOICE")
    elif ch == 2:
        import employee_login
    elif ch == 3:
        import employer_login
    else:
        print("INVALID CHOICE")


main()
