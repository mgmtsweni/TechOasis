from tkinter import * # type: ignore
import sqlite3
from tkinter import messagebox


root = Tk()
root.title('CodSoft')
root.geometry('800x600+10+10')
root.resizable(0, 0) # type: ignore

connection = sqlite3.connect('contactBook.db')
cursor = connection.cursor()

def search():
    if nameEntry.get() == '' and numberEntry.get() == '':
        messagebox.showerror('error:', 'At least one field is required')
    elif nameEntry.get() == '' or numberEntry.get() == '':
        cursor.execute('SELECT * FROM Contacts WHERE id = ? OR store_name = ?', (nameEntry.get(), numberEntry.get()))
        rows = cursor.fetchall()
        if rows:
            resultsList = Listbox(root, width=55, height=15)
            resultsList.place(x=280, y=98)
            for row in rows:
                print(row)
                resultsList.insert(END, f"Store Name:      {row[0]}")
                resultsList.insert(END, f"Phone Number:    {row[1]}")
                resultsList.insert(END, f"Store Email:     {row[2]}")
                resultsList.insert(END, f"Store Address:   {row[3]}")
                resultsList.insert(END, f"Store Id:        {row[4]}")
        else:
            print("not found")
    else:
        messagebox.showerror('error', "Only One field is required")

def main():
    root.destroy()
    import main

btnView = Button(root, text='Back', bd=0, activeforeground='black',
                    bg='white', fg="black", font=('Arial', 15, 'bold'), command=main)
btnView.place(x=20, y=40)

searchFrame = LabelFrame(root, padx=20, pady=80, text="Search for Contact")
searchFrame.place(x=20, y=90)

storeName = Label(searchFrame, text="Enter Store Name")
storeName.grid(row=0,column=0)
nameEntry = Entry(searchFrame, width=20, borderwidth=1)
nameEntry.grid(row=1,column=0)
phoneNumber = Label(searchFrame, text="or \nEnter Store Number")
phoneNumber.grid(row=2,column=0)
numberEntry = Entry(searchFrame, width=20, borderwidth=1)
numberEntry.grid(row=3,column=0)
btn = Button(searchFrame, text="Submit",padx=20, pady=10, command=search)
btn.grid(row=10,column=0)

root.mainloop()

connection.close()
