import mysql.connector
from mysql.connector import Error


def database_connection():
        conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="m4hl4ts3",
                        database="pydata"
                )
        return conn
        '''if conn.is_connected():
                cursor = conn.cursor()
                #cursor.execute('CREATE TABLE IF NOT EXISTS Contacts ( id int NOT NULL AUTO_INCREMENT PRIMARY KEY, store_name VARCHAR(255), phone_number VARCHAR(10), email VARCHAR(255), address VARCHAR(255))')
                #cursor.execute("DROP TABLE Contacts")
                #cursor.execute("SHOW TABLES")
                #cursor.execute("SELECT * FROM Contacts")
        for x in cursor:
                print(x)

if __name__ == "__main__":
        database_connection()

'''