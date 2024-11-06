from tkinter import * # type: ignore
import sqlite3
from tkinter import messagebox


root = Tk()
root.title('CodSoft')
root.geometry('500x600+10+10')
root.resizable(0, 0) # type: ignore

def clear():
    nameEntry.delete(0, END)
    numberEntry.delete(0, END)
    emailEntry.delete(0, END)
    addressEntry.delete(0, END)
    idEntry.delete(0, END)

connection = sqlite3.connect('contactBook.db')
cursor = connection.cursor()

def manu():
    root.destroy()
    import main

def database():
    if nameEntry.get() == '' or numberEntry.get() == '' or \
        emailEntry.get() == '' or addressEntry.get() == '':
        messagebox.showerror('error:', 'all field are required')
    else:
        try:
            query = 'SELECT * FROM Contacts WHERE id = ? OR address = ?'
            cursor.execute(query, (nameEntry.get(), idEntry.get()))
            row = cursor.fetchone()
            if row == None:
                cursor.execute('INSERT INTO Contacts VALUES (:store_name, :phone_number, :email, :address, :id)',
                            {
                                'store_name': nameEntry.get(),
                                'phone_number': numberEntry.get(),
                                'email': emailEntry.get(),
                                'address': addressEntry.get(),
                                'id': idEntry.get()
                            })
                messagebox.showinfo('Success', 'User Registered Successful')
            else:
                messagebox.showerror('Error', 'Data already exist')
        except Exception:
            messagebox.showerror('Error', 'Data already exist')
        finally:
            connection.commit()
            clear()

regFrame = LabelFrame(root, padx=20, pady=80, text="Enter New Contact")
regFrame.place(x=150, y=90)

storeName = Label(regFrame, text="Enter Store Name")
storeName.grid(row=1,column=0)
nameEntry = Entry(regFrame, width=20, borderwidth=1)
nameEntry.grid(row=2,column=0)
phoneNumber = Label(regFrame, text="Enter Phone Number")
phoneNumber.grid(row=3,column=0)
numberEntry = Entry(regFrame, width=20, borderwidth=1)
numberEntry.grid(row=4,column=0)
emailAddress = Label(regFrame, text="Enter Email Address")
emailAddress.grid(row=5,column=0)
emailEntry = Entry(regFrame, width=20, borderwidth=1)
emailEntry.grid(row=6,column=0)
storeAddress = Label(regFrame, text="Enter Store Address")
storeAddress.grid(row=7,column=0)
addressEntry = Entry(regFrame, width=20, borderwidth=1)
addressEntry.grid(row=8,column=0)
storeID = Label(regFrame, text="Enter Store ID")
storeID.grid(row=9,column=0)
idEntry = Entry(regFrame, width=20, borderwidth=1)
idEntry.grid(row=10,column=0)
btn = Button(regFrame, text="Submit",padx=20, pady=10, command=database)
btn.grid(row=11,column=0)
btnExit = Button(regFrame, text="Main Manu",padx=20, pady=10, command=manu)
btnExit.grid(row=0,column=0)


root.mainloop()
connection.close()
