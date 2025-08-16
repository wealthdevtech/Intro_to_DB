# Import the mysql-connector module
import mysql.connector 

# Make connection to SQL Server and handle connection error(s)
try:
    with mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "wealthdevtech",
        database = "alx_book_store"
    ) as alx_book_store:
        print(f"Database 'alx_book_store' created successfully!")
        cursor = alx_book_store.cursor()
        cursor.execute("")
except mysql.connector.Error as e:
    print(e)
