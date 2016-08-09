import os
import sqlite3

db_filename = "Database.db"
schema_filename = "Database_schema.sql" #contains the schema for the database.

db_is_new = not os.path.exists(db_filename) #False if db already exists. True if it does not

#This function prints the basic options available to the suer. It prints these options and returns index of action chosen
def printOptions():
    print("What do you want to do?")
    print("1. Add stocks to your portfolio")        #i.e. enter a purchase of some stocks
    print("2. Remove stocks from your portfolio")   #i.e. enter a sale of some stocks
    print("3. View your activity for a specific stock") #if user is interested in seeing their activity and current holdings in a particular stock
    print("4. View your entire portfolio")
    print("5. Exit")
    x=int(input())
    return x

# NOTE: If user buys the same stock at two different price points, the database stores this as two different transactions.
# Additions/Modifications - 
#   1. After inputting all information, show user summary of transaction and ask to confirm
#   2. Validation for purchase date
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
    print("Transaction successfully entered")
    conn.close()

# function to remove a stock from the portfolio
def processRemove():


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

#This function will create a database which holds the user's activity if this database does not already exist
def createSQLiteDB():
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    if db_is_new:                           #I need to execute the schema only if database doesn't already exist. If there already is a database,
                                            #executing the schema again will be an error
        with open(schema_filename) as f:
            schema = f.read()               
            conn.executescript(schema)     
    conn.commit()
    conn.close()

def main():
    createSQLiteDB()
    selection=printOptions()
    while (selection!=5): #while the user wants to stay in the program
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