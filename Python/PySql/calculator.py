def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def Calculator():
    operations = {
        '1': ('Addition', add),
        '2': ('Subtraction', subtract),
        '3': ('Multiplication', multiply),
        '4': ('Division', divide)
        }

    print("Pick an operator:")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")

    choice = input("Choose your operator: ")
    if choice in operations:
        num1 = int(input('Enter your first number: '))
        num2 = int(input('Enter your second number: '))
        opp_name, opp_func = operations[choice]
        result = opp_func(num1, num2)
        print("Result of", opp_name, ":",result)
    else:
        print("Invalid choice. Please select a valid operator.")

if __name__ == "__main__":
    Calculator()
