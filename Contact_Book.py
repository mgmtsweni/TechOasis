import mysql.connector
import sys
""" Store name, phone number, email, and address for each contact."""


def database_connection():
        connect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="#####",
            database="pydata")
        return connect

def Add_Contact(connection):
    cursor = connection.cursor()
    """Allow users to add new contacts with their details."""
    print("Add a new store contact to the list\n")
    store_name = input("Enter the store name: ").capitalize()
    phone_number = input("Enter store phone number: ")
    email = input("Enter store email address: ")
    address = input("Enter store address: ")
    try:
        cursor.execute('''
        INSERT INTO Contacts (store_name, phone_number, email, address) 
        VALUES (%s, %s, %s, %s)''', (store_name, phone_number, email, address))
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        print("Contact added successfully!")
        cursor.close()
        connection.close()

def View_Contact(connection):
    cursor = connection.cursor()
    """Display a list of all saved contacts with names and phone numbers."""
    try:
        cursor.execute("SELECT * FROM Contacts")
        my_contacts = cursor.fetchall()
        print(cursor.rowcount, "Contact(s) Available.")
        for contact in my_contacts:
            print(contact)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def Search_Contact(connection):
    cursor = connection.cursor()
    """Implement a search function to find contacts by name or phone number"""
    print("Search for a contact by")
    name = input("Enter Store name or leave blank: ")
    phone = input("Enter Phone number or leave blank: ")
    choice = {'store_name': name, 'phone_number': phone}
    params = []

    if choice['store_name']:
        params.append(choice['store_name'])
        try:
            cursor.execute("SELECT * FROM Contacts WHERE store_name = %s", params)
            my_contacts = cursor.fetchall()
            for contact in my_contacts:
                print(contact)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            connection.close()
    elif choice['phone_number']:
        params.append(choice['phone_number'])
        try:
            cursor.execute("SELECT * FROM Contacts WHERE phone_number = %s", params)
            my_contacts = cursor.fetchall()

            for contact in my_contacts:
                print(contact)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            connection.close()
    else:
        print("Invalide entery, try again!!")

def Update_Contact(connection):
    cursor = connection.cursor()
    """Enable users to update contact details."""
    try:
        cursor.execute("SELECT * FROM Contacts")
        my_contacts = cursor.fetchall()

        for contact in my_contacts:
            print(contact)

        print("Select contact item to update.")
        store_name = input("Enter Store name or leave blank: ").capitalize()
        phone_number = input("Enter Phone number or leave blank: ")
        email = input("Enter email address or leave blank: ")
        address = input("Enter location address or leave blank: ")
        choice = {'store_name': store_name,'phone_number': phone_number, 'email': email, 'address': address}

        if choice['store_name']:
            print("#################################")
            store = input("Enter new store name: ").capitalize()
            cursor.execute("UPDATE Contacts SET store_name = %s WHERE store_name = %s", (store, store_name))
            connection.commit()
        elif choice['phone_number']:
            print("#################################")
            phone = input("Enter new phone number: ")
            cursor.execute("UPDATE Contacts SET phone_number = %s WHERE phone_number = %s", (phone, phone_number))
            connection.commit()

        elif choice['email']:
            print("#################################")
            newemail = input("Enter email address or leave blank: ")
            cursor.execute("UPDATE Contacts SET email = %s WHERE email = %s", (newemail, email))
            connection.commit()

        elif choice['address']:
            print("#################################")
            newaddress = input("Enter location address or leave blank: ")
            cursor.execute("UPDATE Contacts SET address = %s WHERE address = %s", (newaddress, address))
            connection.commit()
        
        else:
            print("Invalid option, try again")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        print("Contact updated successfully!")
        cursor.close()
        connection.close()

def done(_):
    sys.exit()

def Delete_Contact(connection):
    cursor = connection.cursor()
    """Provide an option to delete a contact"""
    try:
        cursor.execute("SELECT * FROM Contacts")
        my_contacts = cursor.fetchall()
        print("Select contact ID to delete:")
        for contact in my_contacts:
            print(contact)
        my_Id = input("Enter ID: ")
        choice = {'id': my_Id}
        params = []
        if choice['id']:
            params.append(choice['id'])
            cursor.execute("DELETE FROM Contacts WHERE id = %s", params)
            connection.commit()
        else:
            print("Invalide entery, try again!!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        print("Contact deleted successfully!")
        cursor.close()
        connection.close()

def Contact_Book():
    conn = database_connection()

    if conn.is_connected():
        options = {
        '1': ('Add Contact', Add_Contact),
        '2': ('View Contacts', View_Contact),
        '3': ('Search Contact', Search_Contact),
        '4': ('Update Contact', Update_Contact),
        '5': ('Delete Contact', Delete_Contact),
        '6': ('Exit!!', done)
        }

        print("What would you like to do?")
        for key, (name, _) in options.items():
            print(f"{key}. {name}")
        choice = input("Enter your choice: ")

        if choice in options:
            _, list_func = options[choice]
            list_func(conn)
        else:
            print("Invalid option, try again")

if __name__ == "__main__":
    while True:
        Contact_Book()
