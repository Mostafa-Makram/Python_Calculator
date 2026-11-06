
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero!"
    return a % b

def square_root(a):
    if a < 0:
        return "Error: Negative number!"
    return math.sqrt(a)

def factorial(a):
    if a < 0 or not a.is_integer():
        return "Error: Enter a non-negative integer!"
    return math.factorial(int(a))


operations = {
    "1": ("Addition", add, 2),
    "2": ("Subtraction", subtract, 2),
    "3": ("Multiplication", multiply, 2),
    "4": ("Division", divide, 2),
    "5": ("Power", power, 2),
    "6": ("Modulus", modulus, 2),
    "7": ("Square Root", square_root, 1),
    "8": ("Factorial", factorial, 1)
}

while True:
    print("\n========== PYTHON CALCULATOR ==========")

    for key, (name, _, _) in operations.items():
        print(f"{key}. {name}")

    print("9. Exit")

    choice = input("\nChoose operation: ")

    if choice == "9":
        print("Calculator closed. Goodbye!")
        break

    if choice not in operations:
        print("Invalid choice!")
        continue

    name, function, arguments = operations[choice]

    try:
        a = float(input("Enter number: "))

        if arguments == 2:
            b = float(input("Enter second number: "))
            result = function(a, b)
        else:
            result = function(a)

        print(f"\n{name} Result: {result}")

    except ValueError:
        print("Error: Please enter valid numbers!")

    except OverflowError:
        print("Error: Number is too large!")
