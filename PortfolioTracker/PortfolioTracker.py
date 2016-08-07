import os
import sqlite3

db_filename = "Database.db"
schema_filename = "Database_schema.sql"

db_is_new = not os.path.exists(db_filename) #False if db already exists. True if it does not

#prints options and returns index of action chosen
def printOptions():
    print("What do you want to do?")
    print("1. Add stocks to your portfolio")
    print("2. Remove stocks from your portfolio")
    print("3. Search your portfolio for stock-specific information")
    print("4. View your portfolio")
    print("5. Exit")
    x=int(input())
    return x

def processAdd():
    conn=sqlite3.connect(db_filename)
    cursor = conn.cursor()
    print("Enter stock symbol: ")
    symbol = input()
    print("Enter your date of purchase (MM/DD/YYYY): ")
    date = input()
    print("Enter purchase price: ")
    price = int(input())
    print("Enter number of stocks purchased: ")
    num=int(input())

    cursor.execute("""INSERT INTO UserInfo(stockSymbol, dateofPurchase, avgPurchasePrice, numOfStocks) VALUES(?,?,?,?)""", (symbol, date, price, num,))
    conn.commit()
    print("Transaction successfully completed")
    print("The current status of your portfolio: ")

    cursor.execute("""SELECT * FROM UserInfo""")
    print("Company           Date of Purchase           Average Purchase Price           Number of stocks held")
    for row in cursor:
        print("{0}           {1}           {2}           {3}".format(row[0], row[1], row[2], row[3]))

    conn.close()


def processSearch():
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    cursor.execute("""SELECT DISTINCT stockSymbol FROM UserInfo""")
    for row in cursor:
        print("{0}".format(row[0]))

    conn.close()


#returns True if database is empty. Returns false otherwise
def checkIfEmpty():
    flag = False;
    sql = "SELECT * FROM UserInfo"

    conn=sqlite3.connect(db_filename)
    cursor = conn.cursor()
    cursor.execute(sql)

    if cursor.fetchone() is None:       #if database is empty
        flag=True;

    conn.close()
    return flag

def createSQLiteDB():
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    if db_is_new:                           # I need to create a schema only if database doesn't already exist. If there already is a database,
                                            # creating the schema again will be an error
        with open(schema_filename) as f:
            schema = f.read()               
            conn.executescript(schema)     
    conn.commit()
    conn.close()

def main():
    createSQLiteDB()
    selection=printOptions()
    while (selection!=5):
        if (selection==1):
            processAdd()
        elif (selection==2):
            processRemove()
        elif (selection==3):
            processSearch()
        elif (selection==4):
            processView()
        selection=printOptions()


if __name__ == '__main__':
    main()