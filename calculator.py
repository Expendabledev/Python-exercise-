def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed."
    return x / y
def exponentiation(x, y):
    return x ** y
def floor_divide(x, y):
    if y == 0:
        return "Division by zero is not allowed."
    return x // y
while True:
    print("\nMy pCalculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Floor Division")
    print("7. Quit")

    option = input("Enter your choice (1/2/3/4/5/6/7): ")

    if option == "7":
        print("Goodbye!")
        break

    if option in ("1", "2", "3", "4", "5", "6"):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if option == "1":
            result = add(num1, num2)
        elif option == "2":
            result = subtract(num1, num2)
        elif option == "3":
            result = multiply(num1, num2)
        elif option == "4":
            result = divide(num1, num2)
        elif option == "5":
            result = exponentiation(num1, num2)
        elif option == "6":
            result = floor_divide(num1, num2)

        print("Result:", result)
    else:
        print("Invalid choice. Please select a valid option.")
