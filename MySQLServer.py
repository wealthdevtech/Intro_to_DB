# Import mysql-connector module 
from mysql.connector import Error, connect

# Make connection to SQL Server and handle connection error(s)
try:
    with connect(
        host = "localhost",
        user = "root",
        password = "wealthdevtech",
        database = "alx_book_store"
    ) as alx_book_store:
        print(f"Database 'alx_book_store' created successfully!")
        cursor = alx_book_store.cursor()
        cursor.execute("")
except Error as e:
    print(e)
