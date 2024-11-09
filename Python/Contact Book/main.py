from tkinter import * # type: ignore
import sqlite3
from tkinter import messagebox


root = Tk()
root.title('CodSoft')
root.geometry('950x600+10+10')
root.resizable(0, 0) # type: ignore

connection = sqlite3.connect('contactBook.db')
cursor = connection.cursor()

def clear():
    nameEntry.delete(0, END)
    numberEntry.delete(0, END)
    emailEntry.delete(0, END)
    addressEntry.delete(0, END)

def search():
    root.destroy()
    import searchContact

def addContact():
    root.destroy()
    import addContact

# view section
def Details():
    viewList = Listbox(root, width=45, height=20)
    viewList.place(x=510, y=70)
    
    item = contactList.get(ANCHOR)[7:11]
    cursor.execute('SELECT * FROM Contacts WHERE address = ?', (item,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        viewList.insert(END, f"Store Name:      {row[0]}")
        viewList.insert(END, f"Phone Number:    {row[1]}")
        viewList.insert(END, f"Store Email:     {row[2]}")
        viewList.insert(END, f"Store Address:   {row[3]}")
        viewList.insert(END, f"Store Id:        {row[4]}")

# To delete section
def delete(toDel):
    item = toDel[7:11]
    name = toDel[14:]

    cursor.execute("DELETE FROM Contacts WHERE address = ?",(item,))
    connection.commit()
    messagebox.showinfo('Success', f'{name} was deleted Successful')
  
def notDelete():
    deleteFrame.destroy()

def showDelete():
    toDel = contactList.get(ANCHOR)
    item = toDel[7:11]
    global deleteFrame
    deleteFrame = LabelFrame(root, width=350, height=150, text="Delete Contact")
    deleteFrame.place(x=550, y=70)
    storeName = Label(deleteFrame, text=f"Are you sure you want to delete store No {item}?",)
    storeName.place(x=25, y=10)
    btnYes = Button(deleteFrame, text='No', bd=0, activeforeground='black',
                        bg='white', fg="black", font=('Arial', 15, 'bold'), command=notDelete)
    btnYes.place(x=210, y=50)
    btnNo = Button(deleteFrame, text='Yes', bd=0, activeforeground='black',
                        bg='white', fg="black", font=('Arial', 15, 'bold'), command=lambda: delete(toDel))
    btnNo.place(x=80, y=50)

def notEdit():
    updateFrame.destroy()

def database(item):
    fields = {
        "name": nameEntry.get(),
        "number": numberEntry.get(),
        "email": emailEntry.get(),
        "address": addressEntry.get()
    }

    # Check empty fields
    if all(not field for field in fields.values()):
        messagebox.showerror('Error:', 'At least one field is required')
        return

    def execute_update(field_name, value):
        cursor.execute(f'UPDATE Contacts SET {field_name} = ? WHERE address = ?', (value, item))
        connection.commit()
        clear()

    # Update based on the fields that are filled
    if fields["number"] == '' and fields["email"] == '' and fields["address"] == '':
        execute_update('id', fields["name"])
    elif fields["name"] == '' and fields["email"] == '' and fields["address"] == '':
        execute_update('store_name', fields["number"])
    elif fields["name"] == '' and fields["number"] == '' and fields["address"] == '':
        execute_update('phone_number', fields["email"])
    elif fields["name"] == '' and fields["number"] == '' and fields["email"] == '':
        execute_update('email', fields["address"])
    else:
        # Build a dynamic query based on which fields are filled
        updates = []
        values = []

        if fields["name"]:
            updates.append("id = ?")
            values.append(fields["name"])
        if fields["number"]:
            updates.append("store_name = ?")
            values.append(fields["number"])
        if fields["email"]:
            updates.append("phone_number = ?")
            values.append(fields["email"])
        if fields["address"]:
            updates.append("email = ?")
            values.append(fields["address"])

        if updates:
            update_query = f"UPDATE Contacts SET {', '.join(updates)} WHERE address = ?"
            values.append(item)  # Append 'item' for the WHERE clause
            cursor.execute(update_query, values)
            connection.commit()
            clear()
        else:
            print("You have reached the Abys")
    cursor.execute('SELECT * FROM Contacts WHERE address = ?', (item,))
    contacts = cursor.fetchall()

    for contact in contacts:
        contactList.insert(END, f"New Update ({contact[4]}): {contact[0]}")

def update():
    global updateFrame
    updateFrame = LabelFrame(root, padx=20, pady=40, text="Update Contact")
    updateFrame.place(x=540, y=65)
    field = contactList.get(ANCHOR)
    item = field[7:11]

    global nameEntry, numberEntry, emailEntry, addressEntry

    storeName = Label(updateFrame, text="Enter Store Name")
    storeName.grid(row=1,column=0)
    nameEntry = Entry(updateFrame, width=20, borderwidth=1)
    nameEntry.grid(row=2,column=0)
    phoneNumber = Label(updateFrame, text="Enter Phone Number")
    phoneNumber.grid(row=3,column=0)
    numberEntry = Entry(updateFrame, width=20, borderwidth=1)
    numberEntry.grid(row=4,column=0)
    emailAddress = Label(updateFrame, text="Enter Store Email")
    emailAddress.grid(row=5,column=0)
    emailEntry = Entry(updateFrame, width=20, borderwidth=1)
    emailEntry.grid(row=6,column=0)
    storeAddress = Label(updateFrame, text="Enter Store Address")
    storeAddress.grid(row=7,column=0)
    addressEntry = Entry(updateFrame, width=20, borderwidth=1)
    addressEntry.grid(row=8,column=0)
    btn = Button(updateFrame, text="Submit",padx=10, pady=10, command=lambda: database(item))
    btncancel = Button(updateFrame, text="Cancel",padx=10, pady=10, command=notEdit)
    btn.grid(row=12,column=0)
    btncancel.grid(row=0,column=0)
    clear()

def view():
    global contactList
    contactList = Listbox(root, width=45, height=20)
    contactList.place(x=20, y=70)
    btnView = Button(root, text='More', bd=0, activeforeground='black',
                    bg='white', fg="black", font=('Arial', 15, 'bold'), command=Details)
    btnView.place(x=385, y=70)

    cursor.execute('SELECT * FROM Contacts')
    contacts = cursor.fetchall()

    for contact in contacts:
        contactList.insert(END, f"Store ({contact[4]}): {contact[0]}")

def refresh():
    print("function to refresh everything")

def Exit():
    root.destroy()


btnFrame = LabelFrame(root, width=350, height=150)
btnFrame.place(x=40, y=20)
btnView = Button(btnFrame, text='View', bd=0, activeforeground='black',
                    bg='white', fg="black", font=('Arial', 15, 'bold'), command=view)
btnView.grid(row=1,column=1)
btnErase = Button(btnFrame, text='Delete', bd=0, activeforeground='black',
                    bg='white', fg="black", font=('Arial', 15, 'bold'), command=showDelete)
btnErase.grid(row=1,column=2)

btnEdite = Button(btnFrame, text='Update', bd=0, activeforeground='black',
                    bg='white', fg="black", font=('Arial', 15, 'bold'), command=update)
btnEdite.grid(row=1,column=3)

btnErase = Button(btnFrame, text='Search', bd=0, activeforeground='black',
                    bg='white', fg="black", font=('Arial', 15, 'bold'), command=search)
btnErase.grid(row=1,column=4)

btnEdite = Button(btnFrame, text='Add', bd=0, activeforeground='black',
                    bg='white', fg="black", font=('Arial', 15, 'bold'), command=addContact)
btnEdite.grid(row=1,column=5)

btnEdite = Button(btnFrame, text='Refresh', bd=0, activeforeground='black',
                    bg='white', fg="black", font=('Arial', 15, 'bold'), command=refresh)
btnEdite.grid(row=1,column=6)

btnEdite = Button(btnFrame, text='Exit', bd=0, activeforeground='black',
                    bg='white', fg="black", font=('Arial', 15, 'bold'), command=Exit)
btnEdite.grid(row=1,column=7)

root.mainloop()
connection.close()
