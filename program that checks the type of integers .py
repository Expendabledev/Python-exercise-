def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

number = int(input("Enter an integer: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
if prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
if number< 0:
    print("Factorial is not defined for negative integers.")
else:
    fact = factorial(number)
    print(f"The factorial of {number} is {fact}.")
