
def Calculator():
    from calculator import Calculator
    Calculator()

def ContactBook():
    from Contact_Book import Contact_Book
    Contact_Book()

def Password_Generator():
    pass

def To_do_list():
    pass

def dashboard():
    from landing import dashboard
    dashboard()

def Apps():
    apps = {
        '1': ('To Do List',To_do_list),
        '2': ('Contact Book',ContactBook),
        '3': ('Calculator',Calculator),
        '4': ('Password geneartor',Password_Generator),
        '5': ('Back To Main Manu',dashboard)
    }

    print ('system22 apps')
    for key, (name, _) in apps.items():
        print(f'{key}. {name}')
    choice = input("Enter your choice: ")

    if choice in apps:
       app_name, application = apps[choice]
       print(f'######## Now starting the {app_name} ########')
       application()
    else:
        print("Invalid choice! Please try again.")

Apps()
