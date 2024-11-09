import mysql.connector
import hashlib
from database import database_connection



class UserAuth:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def registration(self):
        """Register a new user with a hashed password."""
        username=self.user
        password=self.password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        conn = database_connection()
        cursor = conn.cursor()

        try:
            cursor.execute('''
            INSERT INTO users (username, password) 
            VALUES (%s, %s)
            ''', (username, hashed_password))
            
            conn.commit()
            print("User registered successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

    def login(self):
        """Authenticate a user by checking the username and password."""
        username=self.user
        password=self.password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        conn = database_connection()
        cursor = conn.cursor()

        cursor.execute('''
        SELECT * FROM users WHERE username = %s AND password = %s
        ''', (username, hashed_password))
        
        user = cursor.fetchone()
        
        cursor.close()
        conn.close()

        if user:
            #if user = admin:
            #Go to admin dashboard
            #else:
            from landing import dashboard
            dashboard()
        else:
            print("Login failed. Check your username and password.")

