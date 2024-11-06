from database import Database


db = Database()
def registration(db, num):
    for _ in range(num):
        username = input('Enter your username: ')
        if username:
            password = input('Enter your password: ')
            confim_password = input('Please confrim your password: ')
            if password != confim_password:
                return print("Passwords do not match")
            else:
                db.add_record(username, password)
        else:
            return print("Username is too short")

def login(db):
    print("Enter your login cradentials")
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    record = db.find_record(username)
    if  record:
        if username == record[0] and password == record[1]:
            print(username, "Has logged in succesfully")
            return username
        else:
            print(f"username or password incorrect. Try again!")
    else:
        print("Register New User")
        registration(db, 1)

def print_all_records(database):
    records = database.get_records()
    print('\nThis are the names in the database:')
    for record in records:
        print(f"Name: {record[0]}, password: {record[1]}")

def my_main(db):
    while True:
        print("Welcome to a simple Python auth system\n")
        print("Choose your options\n1. Login\n2. Register")
        num = int(input("Enter your selection: "))
        if num == 1:
            login(db)
        elif num == 2:
            num_entry = int(input("How individuals are you registering?\n"))
            print("Enter a new user:")
            registration(db, num_entry)
        else:
            print("Invalid option Try again")


my_main(db)
