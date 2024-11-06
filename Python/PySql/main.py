from auth import UserAuth
from database import database_connection
import sys


def main():
    print("\nWelcome to system22\n")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = input("Enter your choice: ")
        
    if choice == '1':
        print("Enter your login cradentials")
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        UserAuth(username, password).login()
    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        confirm_password = input("Confirm your password: ")
        if password != confirm_password:
            return print("Passwords do not match")
        else:
            UserAuth(username, password).registration()
    elif choice == '3':
        sys.exit()
    else:
        print("Invalid choice! Please try again.")



# Example usage
if __name__ == "__main__":
    # Initialize the UserAuth class with your MySQL database credentials
    auth_system = database_connection()
    if auth_system:
        main()
