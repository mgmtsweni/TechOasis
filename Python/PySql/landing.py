from database import database_connection


def dashboard():
    while True:
        print("\nSystem22 Main manu\n")
        print("1. Apps")
        print("2. Games")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            from apps import Apps
            Apps()
        elif choice == '2':
            from games import Games
            Games()
        elif choice == '3':
            from main import main
            main()
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    dashboard()
